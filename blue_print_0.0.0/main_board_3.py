# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : Leon
# created:  2020.7

# Description:
#   Blueprint 技术验证用
#   保存、读取文件的模块
# ------------------------(max to 80 columns)-----------------------------------
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from fm_class_hour import MyFrameHours
from fm_class_weeks import MyFrameWeeks
from fm_class_lamp import MyFrameLamp
from data_class_event import data_class

class board_weekly_show:
    def __init__(self,prent_win):
        self.win=tk.Toplevel()

        self.win.title('Event board')
        win_size_pos = "1000x600"
        self.win.geometry(win_size_pos)
        lbfLamp=MyFrameLamp(self.win,'Alerting',0,0)


        lbfNextHour = MyFrameHours(self.win, 'Events of next hour', 1, 0)
        lbfNextHour8 = MyFrameHours(self.win, 'Events of next 8 hour', 1, 1)
        lbfNextHour12 = MyFrameHours(self.win, 'Events of next 12 hour', 1, 2)
        lbfNextHour24 = MyFrameHours(self.win, 'Events of next 24 hour', 1, 3)

        lbfNextWeek=ttk.Labelframe(
            self.win, text='Events of next week',width=790,height=300)
        lbfNextWeek.grid(row=2, column=0, columnspan=7,padx=5,pady=5,sticky=tk.W)

        lbfDays=[]

        for i in range(7):
            d=datetime.date.today()+datetime.timedelta(days=i+1)
            lbfDay=MyFrameWeeks(lbfNextWeek, d.strftime('%Y-%m-%d'), 0 , 2+i)
            lbfDays.append(lbfDay)

        def refresh_and_alert():
            print('refresh [%s]'% datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lbfNextHour.refresh_events(0,60)
            lbfNextHour8.refresh_events(61,480)
            lbfNextHour12.refresh_events(481,720)
            lbfNextHour24.refresh_events(721,1440)

            for i in range(7):
                lbfDays[i].refresh_events(
                datetime.date.today()+datetime.timedelta(days=i+1))
            lbfLamp.refresh_events()

            self.win.after(5000,refresh_and_alert)
            return

        self.win.after(5000,refresh_and_alert)
        self.win.mainloop()
