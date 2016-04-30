#coding=utf8
"""
@author:kinegratii
2014-04-11
"""
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
 
class Cal(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES,fill = BOTH)
        self.master.title('Calculator By Kinegratii')
        self.master.geometry('400x400')
        self.draw()
         
    def add_button(self,parent,side,text,command = None):
        b = Button(parent,text = text,command = command)
        b.pack(side = side,expand = YES,fill = BOTH)
        return b
 
    def add_frame(self,parent,side):
        f = Frame(parent)
        f.pack(side = side,expand = YES,fill = BOTH)
        return f
 
    def draw(self):
        res = StringVar()
        cc = StringVar()
        e = Entry(self,relief = SUNKEN,textvariable = cc)
        e.pack(side = TOP,expand = YES,fill = BOTH)
        r = Entry(self,relief = SUNKEN,textvariable = res)
        r.pack(side = TOP,expand = YES,fill = BOTH)
        charArray = ("123+","456-","789*","-0./","%()")
        for vx in charArray:
            keyF = self.add_frame(self,TOP)
            for char in vx:
                self.add_button(keyF,LEFT,char,
                               lambda o = cc,s = '%s'%char:self.show_result(o,s))
        self.add_button(keyF,LEFT,'=',lambda o = cc,r = res,s = self:s.cal(o,r))
        keyF = self.add_frame(self,TOP)
        self.add_button(keyF,LEFT,'Clear',
                       lambda o = cc,r = res:(o.set('0'),res.set('0')))
        self.add_button(keyF,LEFT,'Del',
                       lambda o = cc:o.set(o.get()[0:-1]))
        self.add_button(keyF,LEFT,'Demo',None)
        Str = 'By Kinegratii,2013-02-26/Python-V3.2/2.7'
        self.add_button(keyF,LEFT,'Help',lambda r = res:r.set(Str))
 
    def show_result(self,cc,char):
        s = cc.get()
        if s == '0':
            s = ''
        s += char
        cc.set(s)
         
    def cal(self,cc,r):
        try:
            r.set(eval(cc.get()))
        except Exception:
            r.set("ERROR")
         
 
def main():
    Cal().mainloop()
 
if __name__ == '__main__':
    main()
