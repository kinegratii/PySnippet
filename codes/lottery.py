#coding=utf8
"""
A simple lottery app written by Tkinter
@author:kinegratii@gmail.com
"""

import random
from Tkinter import *

class SplashLabel(Label):
    def __init__(self, parent, min_value, max_value, **kwargs):
        Label.__init__(self, parent, text=str(min_value),**kwargs)
        self.min_value = min_value
        self.max_value = max_value
        self._cur_value = min_value
        self._state = False
        self._timer_id = None

    def update_value(self, value):
        self.config({'text': str(value)})

    def set_range_value(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _timer(self):
        if self._state:
            self._cur_value = random.randint(self.min_value, self.max_value + 1)
            self.config({'text': str(self._cur_value)})
            self._timer_id = self.after(100, self._timer)

    def start_splash(self):
         if not self._state:
            self._state = True
            self._timer()

    def stop_splash(self):
        self._state = False
        if self._timer_id:
            self.after_cancel(self._timer_id)
            self._timer_id = None

class LotteryApp(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Lottery App')
        self.master.resizable(False, False)
        self.pack(expand=NO,fill=BOTH)

        min_label = Label(self, text='from')
        min_label.grid(row=0,column=0)
        self.min_value = IntVar()
        self.min_value.set(1)
        self.min_entry = Entry(self, textvariable=self.min_value)
        self.min_entry.grid(row=0, column=1)
        max_label = Label(self, text='to')
        max_label.grid(row=0, column=2)
        self.max_value = IntVar()
        self.max_value.set(50)
        self.max_entry = Entry(self, textvariable=self.max_value)
        self.max_entry.grid(row=0, column=3)

        self.splash_label = SplashLabel(self, 1, 50)
        self.splash_label.grid(row=1, column=0, columnspan=4)

        self.Lottery_btn = Button(self, text='Start', command=self.lottery_handler)
        self.Lottery_btn.grid(row=2, column=0, columnspan=4)
        self.play = False

    def lottery_handler(self):
        if self.play:

            self.splash_label.stop_splash()
            self.Lottery_btn.config({'text': 'Start'})
        else:
            min_value, max_value = self.min_value.get(), self.max_value.get()
            self.splash_label.set_range_value(min_value, max_value)
            self.splash_label.start_splash()
            self.Lottery_btn.config({'text': 'Stop'})
        self.play = not self.play


def main():
    app = LotteryApp()
    app.mainloop()

if __name__ == '__main__':
    main()
