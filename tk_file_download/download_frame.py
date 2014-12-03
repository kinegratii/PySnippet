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
