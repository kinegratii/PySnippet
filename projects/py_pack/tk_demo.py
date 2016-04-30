#coding=utf-8
"""
简单的tkGUI程序
Note:只在python2下有效
"""
from Tkinter import *
import tkMessageBox


class ConfigWindow(Frame):
    def __init__(self, ):
        Frame.__init__(self)
        self.master.title('Tk Demo')
        self.master.geometry('500x300')
        self.master.resizable(False, False)
        self.pack(side = TOP,expand = YES,fill = BOTH)
        bt = Button(self,text='hello',command=self.hello)
        bt.pack(side=TOP,expand=NO,fill=Y,pady=20,padx=20)
    
    def hello(self):
        tkMessageBox.showinfo('Info','Hello,This is a demo for tkinter');
    

if __name__ == '__main__':
    ConfigWindow().mainloop()

    
