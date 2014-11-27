# tkinter文件下载 

## 使用方法

输入下载地址和本地文件名称，默认保存在脚本同一目录下，点击下载按钮开始下载文件同时在果冻条显示当前下载进度。

## 技术要点

(*项目代码仅在Python2.x可用*)

### 文件下载

函数原型：`urllib.urlretrieve(url[, filename[, reporthook[, data]]])`

文档参见[这里](https://docs.python.org/2.7/library/urllib.html#urllib.urlretrieve)

### 线程通信

触发事件 `w.event_generate( sequence, **kw)` ，其sequence为类似于`<<reflash>>`的事件名称。

绑定自定义事件 `self.bind('<<reflash>>',self.onReflashEvent)`

UI线程和子线程共享同一个数据队列，执行过程如下：

向队列写入数据（子线程） - 触发事件（子线程） - 收到事件（UI线程） - 从队列取出数据（UI线程）


## 作者

Kinegratii <kinegratii@gmail.com>