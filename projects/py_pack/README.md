## 1 Python打包工具

目前在windows平台上将Python程序打包成exe文件主要有三个工具。

- py2exe http://www.py2exe.org/
- cx_freeze http://cx-freeze.sourceforge.net/
- PyInstaller http://pythonhosted.org/PyInstaller/

今天将一个Tkinter写的界面程序打包成exe文件，三个工具都试了一遍，感觉PyInstaller会比较好用一些。

## 2 py2exe

### 2.1 下载安装

从这里https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/ 选择python版本和计算机位数对应的exe文件，双击即可安装。

### 2.2 启动脚本

写一个setup_py2exe.py文件

```

from distutils.core import setup
import py2exe
options = {'py2exe': {'compressed': 1,
                      'optimize': 2,
                      'bundle_files': 1, }}
setup(name='App',
      author='kinegratii',
      version='1.0.0',
      options=options,
      windows=[{"script": "app.py"}],
      zipfile=None
      )

```

### 2.3 命令

执行python setup_py2exe.py py2exe即可，dist目录就是最后生成的结果。

### 2.4 Q&A

**import py2exe**

`import py2exe`这个语句要保留，因为用PyCharm自动格式化的时候总会把这个语句优化掉。

**UnicodeDecodeError异常**

之前加了`from __future__ import unicode_literals`这个语句，会报`UnicodeDecodeError: 'utf8' codec can't decode byte 0xd1 in position 3: invalid continuation byte`

**lxml库**

程序报的异常是`ImportError: No module named lxml._elementpath`，但按照网上的说法加了includes参数可以解决。

```
options={
    'py2exe': {
        'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
    }
}
```

**TypeError: expected string or buffer**

这个异常是docx这个库出现的。找了很久还没有什么头绪。

## 3 cx_freeze

### 3.1 pip安装

执行pip命令即可安装

```
pip install cx_Freeze
```

### 3.2 启动脚本

setup_cx.py文件如下

```
from __future__ import unicode_literals
import sys
from cx_Freeze import setup, Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"
includeFiles = [
    (r"D:\py\tcl\tcl8.5", "tcl"),
    (r"D:\py\tcl\tk8.5", "tk")
]
setup(
    name="App",
    version="1.0",
    description="A demo app",
    options={"build_exe": {"include_files": includeFiles, }},
    executables=[Executable("app.py", base=base, includes=['lxml', 'lxml.tree', 'lxml._namepath'])]
)

```

### 3.3 命令

执行命令python setup_cx.py build，dist下的exe.开头的文件夹（名字跟具体环境有关，比如我的是exe.win32-2.7）就是最后的生成的文件夹。

### 3.4 Q&A

**lxml**

也需要明确包含`lxml._elementpath`

**docx**

也出现了和py2exe一样的异常。

## 4 PyInstaller

### 4.1  pip安装

执行pip安装

````
pip install pyinstaller
```

安装成功后在python的目录下\Scripts文件夹多出pyinstaller.exe、pyinstaller.exe.manifest、pyinstaller-script.py等几个文件。

### 4.2 命令方式构建

把Scripts目录加到系统的环境变量中，cd到脚本所在的目录，然后执行下面的命令。

```
pyinstaller app.py -F -w --clean
```

app.py 脚本文件

几个选项含义

- -F 打包为单一文件，和打包为一个文件夹相对，默认为后者
- -w 窗口程序，与控制台相对
- --clean 每次清理中间产生的构建文件

生成的相关文件包括

- app.spec 配置文件
- build文件夹 构建中产生的中间文件
- dist/app文件夹 这里的文件都是运行所需要的

### 4.3 启动脚本方式

命令行带太多参数的话，每次都要输入，比较麻烦，可以统统写在一个py脚本中。

PyInstaller也是一个标准的Python包，提供了`PyInstaller.main.run`这个方法。

4.2节中等效的python脚本如下

```
if __name__ == '__main__':
    from PyInstaller.main import run
    params=[app.py', '-F', '-w', '--clean']
    run(params)
```

用Python解释器执行这个脚本就可以了。

### 4.4 Q&A

**lxml**

可以解决lxml包含的问题，无需明确指定

**调试**

由于用了没有控制台的-w方式，如果程序启动有错的话，只会弹出app return -1的对话框，没有具体异常信息。可以先去掉-w，用控制台进行调试，所有的异常和程序中的print函数就显示在控制台上，方便调试。

**单exe资源文件路径问题**

这个问题应该只要是最后打包成单个exe都会出现的问题。描述如下

最后打包的文件结构如下

```
- XxxApp
    - app.exe
    - data
        - wpa.db
```

程序中用下面语句引用wpa.db文件，会出现文件打不开的情况

```
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_FILE = os.path.join(BASE_DIR,'data', 'wpa.db')
```
调试打印出`BASE_DIR`，发现路径不是XxxApp，而是在用户目录下的某一个位置，类似如下

```
c:\Users\kinegratii\AppData'Local\Temp\_MEI11~1\dadta\wpa.db
```

这是因为**在单文件模式中运行程序的时候先将文件解压到sys._MEIPASS指向的目录下，所以引用资源文件就需要添加os.path.join(sys._MEIPASS,filename)**，

第一种方法，具体判断程序当前模式。

```
  if getattr(sys, 'frozen', False):
        BASE_DIR = sys._MEIPASS
    else:
        BASE_DIR = os.path.dirname(__file__)
```

第二种，就是将`__file__`改为sys.args[0]，即

```
BASE_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
```

这样打印的路径就是正确的了，原因在于`__file__`和`sys.args[0]`有点区别。

> `__file__` is the name of the current file, which may be different from the main script if you are inside a module or if you start a script using execfile() rather than by invoking python scriptname.py.  `__file__` is generally your safer bet.

来自 http://stackoverflow.com/a/5851608


**icon图标无法显示问题**

使用icon选项即可添加图标，但有时候发现资源管理器的图标可以显示，但运行程序后任务栏上的图标却无法显示。关于这个问题 。

> 在不同情况下（比如资源管理器文件列表前面的图标、桌面、开始菜单等）需要不一样尺寸的图标。如果尺寸不合适的话，可能出现有的地方显示正确有的显示不正确的情况。最后几个地方都要检查一遍。

解决方案

> 应该准备四张不同尺寸（具体尺寸参见 http://stackoverflow.com/questions/3236115/which-icon-sizes-should-my-windows-applications-icon-include ）的png文件
用png2icon脚本把它们合成一张icon图标文件即可



## 5 参考资料

- py2exe lxml error http://stackoverflow.com/a/5309733
- Creating an Executable from a Python Script | Matt Borgerson
https://mborgerson.com/creating-an-executable-from-a-python-script
- pyinstaller打包pyqt文件 - dcb3688 - 博客园
http://www.cnblogs.com/dcb3688/p/4211390.html
- 使用pyinstaller打包python程序 - 魏哲的空间
https://blog.weizhe.net/?p=412
