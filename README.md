# PySnippet

（个人Python代码片段）

*Last Updated on 8th Feb.2015*

## Python

### What is Python

Python is a dynamic, interpreted language. Source code does not declare the types of variables or parameters or methods. This makes the code short and flexible, and you lose the compile-time type checking in the source code. Python tracks the types of all values at runtime and flags code that does not make sense as it runs. 

> Source :<https://developers.google.com/edu/python/introduction>

### Python Guide

The following reference links collects many books/blogs/websites for python guide.

* [Python-Guide](http://docs.python-guide.org/en/latest/intro/learning/)
* [BeginnersGuide/NonProgrammers - Python Wiki](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
* [Offical Python Guide](https://docs.python.org/2/tutorial/index.html)
* [Tkinter 8.5 Reference:a GUI for python](http://www.nmt.edu/tcc/help/pubs/tkinter/)
* [An Introduction to Tkinter(Work in Progress)](http://effbot.org/tkinterbook/) 

## What is There

This project contains lots of snippets when learning and working,which may be helpful for python beginners.

### 基础语法

* [`basic/for_else_demo.py`](https://github.com/kinegratii/PySnippet/blob/master/basic/for_else_demo.py) （for-else用法示例）
* [`basic/ab_gucess.py`](https://github.com/kinegratii/PySnippet/blob/master/basic/ab_gucess.py)（xAyB猜数字游戏）

### json -- python对象和json数据转化

```python

    import json
    data = {'name':'John','age':24}
    json.dumps(data)
```

> [`obj2json`](https://github.com/kinegratii/PySnippet/tree/master/obj2json) （嵌套对象转化为JSON，自定义JSONEncoder）

### Tkinter -- Python内置的GUI工具库


* [`basic/calculator.py`](https://github.com/kinegratii/PySnippet/blob/master/basic/calculator.py) （tk计算器）
* [`minesweeper`](https://github.com/kinegratii/minesweeper)（扫雷游戏tk版） 

### urllib2 -- 获取网络数据和爬虫基础

```python
    
    ip = '221.23.34.34'
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip={ip}'.format(ip=ip)
    req = urllib2.Request(url)
    try:
        response_str = urllib2.urlopen(req)
        if response_str:
            res = json.load(response_str)           
    except Exception as e:
        print str(e)
```

### re -- 正则表达式

* [`tk_file_download`](https://github.com/kinegratii/PySnippet/tree/master/tk_file_download)（文件下载tk版）
* [`ip_query`](https://github.com/kinegratii/PySnippet/tree/master/ip_query)（IP归属地查询tk版）

### Socket/SocketServer/Threading -- 网络编程和多线程

* [`tcp2tcp`](https://github.com/kinegratii/PySnippet/tree/master/tcp2tcp)（TCP数据双向中转器）

```python

	class TCPForwardServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	    def __init__(self, bind_port, handler):
	        SocketServer.TCPServer.__init__(self, (LOCAL_HOST, bind_port), handler)
```

### py2exe -- 部署打包

* [`py_pack/py2exe_tk_setup.py`](https://github.com/kinegratii/PySnippet/blob/master/py_pack/py2exe_tk_setup.py) (py2exe打包tk程序打包脚本）
* [`py_pack/cx_tk_setup.py`](https://github.com/kinegratii/PySnippet/blob/master/py_pack/cx_tk_setup.py) (cx_freeze打包tk程序打包脚本）

```python

	from distutils.core import setup
	import py2exe
	
	options = {'py2exe':{'compressed':1,
	                     'optimize':2,
	                     'bundle_files':1,}}
	
	setup(name = 'tk_demo',
	      author = 'kinegratii',
	      author_email = 'kinegratii@gmail.com',
	      version = '1.0.0',
	      options = options,
	      windows=[{"script":"tk_demo.py"}],
	      zipfile = None
	      )
```
 
## How To Use

### Useage

This Project consists of independently packages/folder and each package can be ran by itself.Read the READ.md file under each package/folder.

### License

This project is based on MIT License (MIT).

## Contacts

Author : Kinegratii

Homepage: KgBlog <http://kinegratii.com>

Tag of Python:[`Django`](https://www.djangoproject.com/) [`tkinter/Tkinter`](https://docs.python.org/2.7/library/tkinter.html)

Email : <kinegratii@gmail.com> or <kinegratii@yeah.net>