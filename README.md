# PySnippet

![Kinegratii](images/head_small.jpg)

*Last Updated on 4th June.2015*

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

### Basic Practices for Gramar

* [`basic/for_else_demo.py`](https://github.com/kinegratii/PySnippet/blob/master/basic/for_else_demo.py) 
* [`basic/ab_gucess.py`](https://github.com/kinegratii/PySnippet/blob/master/basic/ab_gucess.py)

### Json

```python

    import json
    data = {'name':'John','age':24}
    json.dumps(data)
```

> [`obj2json`](https://github.com/kinegratii/PySnippet/tree/master/obj2json) A object-nested JSONEncoder

### Tkinter -  A Buildin GUI


* [`basic/calculator.py`](https://github.com/kinegratii/PySnippet/blob/master/basic/calculator.py)

### urllib2 -- Network

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

### re -  Regular expression operations

* [`tk_file_download`](https://github.com/kinegratii/PySnippet/tree/master/tk_file_download)
* [`ip_query`](https://github.com/kinegratii/PySnippet/tree/master/ip_query)

### Socket/SocketServer/Threading

* [`tcp2tcp`](https://github.com/kinegratii/PySnippet/tree/master/tcp2tcp)

```python

	class TCPForwardServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	    def __init__(self, bind_port, handler):
	        SocketServer.TCPServer.__init__(self, (LOCAL_HOST, bind_port), handler)
```

### py2exe

* [`py_pack/py2exe_tk_setup.py`](https://github.com/kinegratii/PySnippet/blob/master/py_pack/py2exe_tk_setup.py) A demo for py2exe
* [`py_pack/cx_tk_setup.py`](https://github.com/kinegratii/PySnippet/blob/master/py_pack/cx_tk_setup.py) A demo for cx_freeze

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
 
## Useage

This Project consists of independently packages/folder and each package can be ran by itself.Read the READ.md file under each package/folder.

## License


```
	
The MIT License (MIT)

Copyright (c) 2014 kinegratii(kinegratii@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```



## Contacts

Author : Kinegratii

Homepage: KgBlog <http://kinegratii.com>

Tag of Python:[`Django`](https://www.djangoproject.com/) [`tkinter/Tkinter`](https://docs.python.org/2.7/library/tkinter.html)

Email : <kinegratii@gmail.com> or <kinegratii@yeah.net>