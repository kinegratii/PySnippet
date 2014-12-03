#coding=utf8

import json
import urllib2
import threading
import Queue
from Tkinter import *
import tkMessageBox


class Event(object):
    REQUEST_COMPLETE = '<<Complete>>'

class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('IP地址查询')
        self.master.geometry('200x240')
        self.master.resizable(False, False)
        self.pack(side = TOP, expand = NO, fill = BOTH)

        self.q = Queue.Queue()

        self.item = ('country','area', 'region', 'city', 'isp', 'ip', 'validate_msg')
        self.data = {k:StringVar() for k in self.item }
        
        Label(self, text='IP地址查询').grid(row=0,column=0, columnspan=5)
        Label(self, text='地址').grid(row=1, column=0, columnspan=1)
        Entry(self, textvariable=self.data['ip']).grid(row=1, column=1, columnspan=4)
        Label(self, text='', textvariable=self.data['validate_msg']).grid(row=2,column=0, columnspan=5)
        Label(self, text='结果').grid(row=3, column=0, columnspan=5)
        Label(self, text='国家').grid(row=4, column=0, columnspan=1)
        Entry(self, textvariable=self.data['country']).grid(row=4, column=1, columnspan=4)
        Label(self, text='地区').grid(row=5, column=0, columnspan=1)
        Entry(self, textvariable=self.data['area']).grid(row=5, column=1, columnspan=4)
        Label(self, text='省').grid(row=6, column=0, columnspan=1)
        Entry(self, textvariable=self.data['region']).grid(row=6, column=1, columnspan=4)
        Label(self, text='市').grid(row=7, column=0, columnspan=1)
        Entry(self, textvariable=self.data['city']).grid(row=7, column=1, columnspan=4)
        Label(self, text='运营商').grid(row=8, column=0, columnspan=1)
        Entry(self, textvariable=self.data['isp']).grid(row=8, column=1, columnspan=4)
        self.query_btn = Button(self, text='查询', command=self.query)
        self.query_btn.grid(row=9, column=0, columnspan=5, sticky=N+E+S+W)
        self.bind(Event.REQUEST_COMPLETE, self.on_complete)

    def query(self):
        self.data['validate_msg'].set('')
        ip =  self.data['ip'].get()
        ipRex = '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
        tmp = re.findall(re.compile(ipRex),ip)
        if not tmp:
            self.data['validate_msg'].set('ip格式错误，请重新输入')
            return
        self.query_btn['state'] = DISABLED
        threading.Thread(target=self.request_ip_address,args=(ip,)).start()
        data = self.request_ip_address(ip)

    def on_complete(self, event):
        self.query_btn['state'] = NORMAL
        data = self.q.get()
        if data.get('code',-1) == 0:
            address_dict = data['data']
            for i in self.item[0:5]:
                self.data[i].set(address_dict[i])
        else:
            self.data['validate_msg'].set('解析失败')


    def request_ip_address(self, ip):
        res = None
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip={ip}'.format(ip=ip)
        req = urllib2.Request(url)
        try:
            response_str = urllib2.urlopen(req)
            if responseStr:
                res = json.load(response_str)           
        except Exception:
            pass
        self.q.put(res)
        try:
            self.event_generate(Event.REQUEST_COMPLETE, when='tail')
        except TclError:
            pass


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
