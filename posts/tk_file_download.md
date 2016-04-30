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

## 代码

```
# -*- coding: UTF-8 -*-
"""TK版文件下载
技术要点：1 自定义事件；2 UI线程和子线程数据通信
"""
from Tkinter import *
import sys,os
import urllib
import threading
import Queue
import tkMessageBox


class Event(object):
    REFLASH = '<<Reflash>>'

class MWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Download Demo')
        self.master.geometry('500x400')
        self.master.resizable(False, False)
        self.grid()
        #下载地址标签、输入框
        self.download_url = StringVar()
        Label(self, text='下载地址').grid(row=0, column=0, columnspan=3, sticky = W+E+N+S)
        Entry(self, textvariable=self.download_url).grid(row=0,column=3, columnspan=7, sticky = W+E+N+S)

        #另存为标签、输入框
        Label(self, text='另存为').grid(row=1, column=0, columnspan=3, sticky = W+E+N+S)
        self.file_name = StringVar()
        Entry(self, textvariable=self.file_name).grid(row=1, column=3, columnspan=7, sticky = W+E+N+S)

        #进度条
        self.scale=Scale(self, from_=0,to=100,orient=HORIZONTAL)
        self.scale.set(0)
        self.scale.grid(row=2, column=0, columnspan=10, sticky = W+E+N+S)
        #按钮
        Button(self, text='下载', command=self.download).grid(row=3, column=3, columnspan=4, sticky = W+E+N+S)
        self.bind(Event.REFLASH,self.on_processing)

    def on_processing(self,event):
        self.scale.set(cq.get())

    def download(self):
        url = self.download_url.get()
        fileName = self.file_name.get()
        if not url or not fileName:
            tkMessageBox.showerror('错误','请填写完整')
            return 0
        self.downThread = threading.Thread(target=downloadTask,args=(url,fileName))
        self.downThread.start()

mw = MWindow()
cq = Queue.Queue()
def downloadTask(url,file_name):
        urllib.urlretrieve(url, fileName, file_name)

def putPercent(downloaded, data_size,file_size):
    """
        downloaded,已下载的数据块
        data_size,数据块的大小
        file_size,远程文件的大小
    """
    perc = 100.0 * downloaded * data_size/file_size
    if 100 < perc:
        perc = 100
    cq.put(perc)
    try:
        mw.event_generate(Event.REFLASH, when='tail')
    except TclError:
        pass

def main():
    mw.mainloop()

if __name__ == '__main__':
    main()

```
