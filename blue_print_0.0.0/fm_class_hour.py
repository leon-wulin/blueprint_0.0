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


class MyFrameHours:
    max_show_events = 8
    max_show_event_name_lenth = 10
    max_progress_len = 120

    def __init__(self, pwin, title, grid_x, grid_y):
        self.pwin = pwin
        lbfHours = ttk.Labelframe(
            pwin, text=title, width=200, height=self.max_show_events * 15)
        lbfHours.grid(row=grid_x, column=grid_y, padx=5, pady=5, sticky=tk.W)
        self.times = []
        self.names = []
        self.progs = []
        for row in range(self.max_show_events):
            t = tk.Label(lbfHours, text='HH:MM:SS')
            t.grid(row=row, column=0, padx=5, pady=5, stick=tk.W)
            self.times.append(t)

            n = tk.Label(lbfHours, text='event name ...')
            n.grid(row=row, column=1, padx=5, pady=5, stick=tk.W)
            self.names.append(n)

            p = ttk.Progressbar(
                lbfHours,
                orient='horizontal',
                length=self.max_progress_len,
                mode='determinate',
                maximum=self.max_progress_len
            )
            p.grid(row=row, column=2, padx=5, pady=5)
            self.progs.append(p)

        return

    def refresh_events(self, fm, to):
        start_dt = datetime.datetime.now() + datetime.timedelta(minutes=fm)
        end_dt = datetime.datetime.now() + datetime.timedelta(minutes=to)
        print('refresh period[%s]-[%s]' % (start_dt, end_dt))

        hours_events = read_period_events(start_dt, end_dt)

        sort_events(hours_events)

        show_num = len(hours_events)
        for i in range(self.max_show_events):
            if i < show_num:
                self.times[i]['text'] = hours_events[i].fm.strftime('%H:%M:%S')
                s = hours_events[i].name
                if len(s) > self.max_show_event_name_lenth:
                    self.names[i]['text'] = s[0:self.max_show_event_name_length] + '...'
                else:
                    self.names[i]['text'] = hours_events[i].name
                diff = hours_events[i].fm - datetime.datetime.now()
                per = diff / datetime.timedelta(minutes=to)
                self.progs[i]['value'] = round(per * self.max_progress_len)
            else:
                self.times[i]['text'] = ''
                self.names[i]['text'] = ''
                self.progs[i]['value'] = 0
        return
