# -*- coding: UTF-8 -*-

import os
import codecs
import random
import datetime

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from mod_event import*
from data_class_event import data_class


class RepeatedEventWindow:
    interval_of_remind = ('never', '0 min', '5 min',
                          '15 min', '30 min', '1 day', '1 week')
    text_of_btn = ( 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.','Sun.')
    value_of_btn = (0, 1, 2, 3, 4, 5, 6)

    def __init__(self, parent_win):

        pop_win = tk.Toplevel()
        pop_win.title('Pop up window test')

        background = tk.Frame(pop_win, bg='#66ccff', width=500, height=500)
        background.place(x=0, y=0)

        self.txtName = tk.StringVar(value='event name')
        self.txtName = tk.Entry(pop_win, textvariable=self.txtName, width=20)
        self.txtName.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.txtFrom = tk.StringVar(value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.txtFrom = tk.Entry(pop_win, textvariable=self.txtFrom, width=20)
        self.txtFrom.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(pop_win, text="to", bg='#66ccff', font=('Arial', 12)).grid(
            row=1, column=1, padx=5, pady=5)

        self.txtTo = tk.StringVar(value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.txtTo = tk.Entry(pop_win, textvariable=self.txtTo, width=20)
        self.txtTo.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

        tk.Label(pop_win, text="remind me", bg='#66ccff', font=('Arial', 12)).grid(
            row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.cmdRemind = ttk.Combobox(pop_win, width=20, state='readonly')
        self.cmdRemind['values'] = ('never', '0 min', '5 min', '10 min')

        self.cmdRemind.grid(
            row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.cmdRemind.current(0)

        lbfConds = ttk.Labelframe(
            pop_win, text='repeatable settings', width=330, height=200)
        lbfConds.grid(row=3, column=0, columnspan=3,
                      padx=5, pady=5, sticky=tk.W)

        lbfByEveryDay = ttk.Labelframe(
            lbfConds, text='Repeat every', width=300, height=40)
        lbfByEveryDay.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.txteveryday= tk.StringVar(value=0)
        self.txteveryday = tk.Entry(
            lbfByEveryDay, textvariable=self.txteveryday, width=20)
        self.txteveryday.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(lbfByEveryDay, text="days", bg='#66ccff', font=('Arial', 12)).grid(
            row=0, column=1, padx=5, pady=5)

        lbfByEveryWeek = ttk.Labelframe(
            lbfConds, text='Repeat every', width=300, height=40)
        lbfByEveryWeek.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.rad_selected_week_day = tk.IntVar()

        for idx in range(7):
            rad_btn = tk.Radiobutton(
                lbfByEveryWeek,
                variable=self.rad_selected_week_day,
                text=self.text_of_btn[idx],
                value=self.value_of_btn[idx],
                command=self.__pick_week_day
            )
            rad_btn.grid(row=0, column=idx, padx=5, pady=5)

        lbfByWeekDay = ttk.Labelframe(
            lbfConds, text='Repeat every', width=300, height=40)
        lbfByWeekDay.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        v0 = tk.IntVar()
        v1 = tk.IntVar()
        v2 = tk.IntVar()
        v3 = tk.IntVar()
        v4 = tk.IntVar()
        v5 = tk.IntVar()
        v6 = tk.IntVar()
        self.value_of_chk = (v0, v1, v2, v3, v4, v5, v6)
        self.chk_selected_week_day = ''
        for idx in range(7):
            chk_btn = tk.Checkbutton(
                lbfByWeekDay,
                text=self.text_of_btn[idx],
                variable=self.value_of_chk[idx],
                command=self.__pick_several_week_days
            )
            chk_btn.grid(row=0, column=idx, padx=5, pady=5)

        lbfByEveryDay = ttk.Labelframe(
            lbfConds, text='Repeat every', width=300, height=40)
        lbfByEveryDay.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.txtmonthday = tk.StringVar(value=0)
        self.txtmonthday  = tk.Entry(
            lbfByEveryDay, textvariable=self.txtmonthday , width=20)
        self.txtmonthday .grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(lbfByEveryDay, text="(th)day of the moneth",
                 bg='#66ccff', font=('Arial', 12)).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.cmdAdd = tk.Button(pop_win, text='Add a repeated event', command=self.__write_to_file).grid(
            row=4, column=1, padx=5, pady=5, sticky=tk.W)
        return

    def __write_to_file(self):

        e_obj = self.__set_data()
        add_event_defination(e_obj)
        return

    def __set_data(self):
        e_obj = data_class()
        print(e_obj.id)
        e_obj.name = self.txtName.get()
        e_obj.type=1
        e_obj.fm = self.txtFrom.get()
        e_obj.to = self.txtTo.get()
        e_obj.remind = self.cmdRemind.get()
        e_obj.every_day=self.txteveryday.get()
        e_obj.every_week_day = self.rad_selected_week_day.get()
        e_obj.week_day= self.chk_selected_week_day
        e_obj.month_day=self.txtmonthday.get()
        print(e_obj.every_week_day)
        return e_obj

    def __pick_several_week_days(self):
        self.chk_selected_week_day=''
        for idx,v in enumerate(self.value_of_chk):
            print(idx,"-",v.get())
            self.chk_selected_week_day+='%d'%v.get()
        #    if v.get()==True:
        #        self.chk_selected_week_day+='%s'%self.text_of_btn[idx]
        print(self.chk_selected_week_day)
        return
    def __pick_week_day(self):
        v = self.rad_selected_week_day.get()
        print(self.text_of_btn[v], self.value_of_btn[v])
        return
