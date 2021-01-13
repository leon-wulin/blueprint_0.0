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

class SingleEventWindow:
    def __init__(self, parent_win):


        pop_win = tk.Toplevel()
        pop_win.title('Pop up window test')

        background = tk.Frame(pop_win, bg='#66ccff', width=500, height=150)
        background.place(x=0, y=0)

        self.txtName = tk.StringVar(value='event name')
        self.txtName = tk.Entry(pop_win, textvariable=self.txtName, width=20)
        self.txtName.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.txtFrom = tk.StringVar(value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.txtFrom = tk.Entry(pop_win, textvariable=self.txtFrom, width=20)
        self.txtFrom.grid(row=2, column=0, padx=5, pady=5)

        tk.Label(pop_win, text="to", bg='#66ccff', font=('Arial', 12)).grid(
            row=2, column=1, padx=5, pady=5)

        self.txtTo = tk.StringVar(value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.txtTo = tk.Entry(pop_win, textvariable=self.txtTo, width=20)
        self.txtTo.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)

        tk.Label(pop_win, text="remind me", bg='#66ccff', font=('Arial', 12)).grid(
            row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.cmdRemind = ttk.Combobox(pop_win, width=20, state='readonly')
        self.cmdRemind['values'] = ('never', '0 min', '5 min', '10 min')

        self.cmdRemind.grid(
            row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.cmdRemind.current(0)

        self.cmdAdd = tk.Button(pop_win, text='Add a single event', command=self.__write_to_file).grid(
            row=4, column=1, padx=5, pady=5, sticky=tk.W)
        return


    def __write_to_file(self):
        '''
        add_a_single_event(
            self.txtName.get(),
            self.txtFrom.get(),
            self.txtTo.get(),
            self.cmdRemind.get()
            )
        '''
        e_obj=self.__set_data()
        add_event_defination(e_obj)
        return


    def __set_data(self):
        e_obj= data_class()
        print(e_obj.id)
        e_obj.name=self.txtName.get()
        e_obj.type=0
        e_obj.fm=self.txtFrom.get()
        e_obj.to=self.txtTo.get()
        e_obj.remind=self.cmdRemind.get()
        return e_obj
