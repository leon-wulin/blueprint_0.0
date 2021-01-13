# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : Leon
# created:  2020.7

# Description:
#   Blueprint 技术验证用
#   保存、读取文件的模块
# ------------------------(max to 80 columns)-----------------------------------

import os
import codecs
import random
import datetime
import calendar
import csv
import copy
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

from mod_event import*

class MyFrameWeeks:
    max_show_events=10
    max_show_event_name_lenth=10
    max_progress_len=120

    def __init__(self,pwin,title,grid_x,grid_y):
        self.pwin=pwin
        lbfDay=ttk.Labelframe(
            pwin,text=title,width=250,height=self.max_show_events*15)
        lbfDay.grid(row=grid_x,column=grid_y,padx=5,pady=5,sticky=tk.W)
        self.times=[]
        self.names=[]
        self.progs=[]
        for row in range(self.max_show_events):
            t=tk.Label(lbfDay,text='HH:MM:SS')
            t.grid(row=row,column=0,padx=5,pady=5,stick=tk.W)
            self.times.append(t)

            n=tk.Label(lbfDay,text='event name ...')
            n.grid(row=row,column=1,padx=5,pady=5,stick=tk.W)
            self.names.append(n)


        return

    def refresh_events(self,that_day):
        start_dt = datetime.datetime(that_day.year,that_day.month,that_day.day,0,0,0)

        end_dt = datetime.datetime(that_day.year,that_day.month,that_day.day,23,59,59)
        print('Weeks refresh period[%s]-[%s]' % (start_dt, end_dt))

        weeks_events = read_period_events(start_dt, end_dt)
        print('Fetched %d events'% len(weeks_events))

        sort_events(weeks_events)

        show_num = len(weeks_events)
        for i in range(self.max_show_events):
            if i < show_num:
                self.times[i]['text'] = weeks_events[i].fm.strftime('%H:%M:%S')
                s = weeks_events[i].name
                if len(s) > self.max_show_event_name_lenth:
                    self.names[i]['text'] = s[0:self.max_show_event_name_length] + '...'
                else:
                    self.names[i]['text'] = weeks_events[i].name

            else:
                self.times[i]['text'] = ''
                self.names[i]['text'] = ''
        return
