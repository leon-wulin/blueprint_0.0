# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from win_class_single_event import SingleEventWindow
from win_class_repeated_event import RepeatedEventWindow
from mod_event import*
from show_events_by_month import show_events_by_month
from main_board_3 import board_weekly_show

class MainWindow:

    def __init__(self, mywin):
        self.win = mywin
        mywin.title('blueprint(POC)')

        win_size_pos='800x600'

        mywin.geometry(win_size_pos)



        #-------------------------------------------------------------------------------
        top_menu=tk.Menu(mywin)
        set_menu=tk.Menu(top_menu,tearoff=False)
        top_menu.add_cascade(label=" Set |",menu=set_menu)
        set_menu.add_command(label="Quit",command=mywin.quit)

        event_menu=tk.Menu(top_menu,tearoff=False)
        top_menu.add_cascade(label=" Modify |",menu=event_menu)

        event_menu.add_command(label="Add a single event",command=self.__cmd_pop_single)
        event_menu.add_command(label="Add a repeated event",command=self.__cmd_pop_repeat)
        event_menu.add_separator()
        event_menu.add_command(label="Del a single event",command=None)
        event_menu.add_command(label="Del a repeated event",command=None)


        view_menu=tk.Menu(top_menu,tearoff=False)
        top_menu.add_cascade(label=" Show  |",menu=view_menu)
        view_menu.add_command(label="show the events weekly",command=self.__cmd_board_weekly_show)
        view_menu.add_command(label="show the events monthly",command= self.__cmd_show_events_by_month)
        view_menu.add_command(label="show the events yearly",command=None)
        view_menu.add_separator()
        view_menu.add_command(label="show all events defination",command=self.__show_all_events_defination)
        view_menu.add_command(label="generate all events",command=self.__cmd_generate_all_events)
        mywin.config(menu=top_menu)
        #-------------------------------------------------------------------------------
        return

    def __cmd_generate_all_events(self):
        all_ed=read_all_events_defination()
        generate_all_events(all_ed)
        return

    def __cmd_pop_single(self):
        sw=SingleEventWindow(self.win)
        return
    def __cmd_pop_repeat(self):
        sw=RepeatedEventWindow(self.win)
        return
    def __show_all_events_defination(self):
        all_events= read_all_events_defination()
        return
    def __cmd_show_events_by_month(self):
        all_ed=show_events_by_month(self.win)
        return

    def __cmd_board_weekly_show(self):
        weekly_show= board_weekly_show(self.win)
