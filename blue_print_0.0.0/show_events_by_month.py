# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
import codecs
import random
import datetime
import calendar
import csv
import copy
from mod_event import*


calendar_span = 60


class show_events_by_month():

    def __init__(self, prent_win):

        self.win = tk.Toplevel()
        self.win.title('show events in one month')

        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        width = 810
        height = 800

        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2

        self.win.geometry('%dx%d+%d+%d' % (width, height, left, top))

        lblHeader = tk.Label(self.win, height=3, bg="#66ccff")
        lblHeader.grid(row=0, column=0, columnspan=7)

        self.btnPreMonth = tk.Button(lblHeader, text='<- last month',
                                     command=self.__show_pre_month)
        self.btnPreMonth.grid(row=0, column=0, padx=10, pady=5)

        s = datetime.datetime.now().strftime("%Y/%m")

        self.lblCurrentMonth = tk.Label(lblHeader, text=s)
        self.lblCurrentMonth.grid(row=0, column=1, padx=10, pady=5)
        self.dtCurrentYMD = datetime.date.today()
        self.btnNextMonth = tk.Button(lblHeader, text='nextmonth ->',
                                      command=self.__show_next_month)
        self.btnNextMonth.grid(row=0, column=2, padx=10, pady=5)

        lbl1 = tk.Label(self.win, text="Monday", width=10, height=2, bg='red').grid(
            row=2, column=0, padx=10, pady=0)

        lbl2 = tk.Label(self.win, text="Tuesday", width=10, height=2, bg='orange').grid(
            row=2, column=1, padx=10, pady=0)

        lbl3 = tk.Label(self.win, text="Wednesday", width=10, height=2, bg='yellow').grid(
            row=2, column=2, padx=10, pady=0)

        lbl4 = tk.Label(self.win, text="Thursday", width=10, height=2, bg='green').grid(
            row=2, column=3, padx=10, pady=0)

        lbl5 = tk.Label(self.win, text="Friday", width=10, height=2, bg='#3CA9C4').grid(
            row=2, column=4, padx=10, pady=0)

        lbl6 = tk.Label(self.win, text="Saterday", width=10, height=2, bg='blue').grid(
            row=2, column=5, padx=10, pady=0)

        lbl7 = tk.Label(self.win, text="Sunday", width=10, height=2, bg='purple').grid(
            row=2, column=6, padx=10, pady=0)

        self.btnAlldays = []
        for i in range(3, 9):
            for k in range(7):
                day_no = '%d th.day' % ((i - 3) * 7 + k)
                btn = tk.Button(self.win, text=day_no, width=10, height=5,
                                # activebackground='white',
                                anchor=tk.NW, relief='groove', command=None)
                btn.grid(row=i, column=k, padx=10, pady=0)
                self.btnAlldays.append(btn)

        self.__refresh_calendar1(datetime.date.today().year,
                                 datetime.date.today().month)
        self.__refresh_calendar2(datetime.date.today().year,
                                 datetime.date.today().month)
        return

    def __refresh_calendar1(self, yyyy, mm):
        blIsCurrentMonth = False

        m_range = calendar.monthrange(yyyy, mm)
        m_start_day = m_range[0]
        days_of_month = m_range[1]

        calendar_start_date = datetime.date(
            yyyy, mm, 1) - datetime.timedelta(days=m_start_day)
        calendar_end_date = calendar_start_date + datetime.timedelta(days=41)
        print('DEBUG,-Show events from %s to %s' %
              (calendar_start_date, calendar_end_date))

        for i in range(0, m_start_day):
            btn = self.btnAlldays[i]
            btn['text'] = '%d/%d' % (calendar_start_date.month,
                                     calendar_start_date.day + i)
            if (self.dtCurrentYMD.month == datetime.date.today().month) and (self.dtCurrentYMD.year == datetime.date.today().year):
                btn['bg'] = '#888888'
                btn['state'] = 'disabled'
            else:
                btn['bg'] = 'lightgreen'
                btn['state'] = 'active'

        for i in range(1, days_of_month + 1):
            btn = self.btnAlldays[m_start_day + i - 1]

            if(i == datetime.date.today().day) and (self.dtCurrentYMD.month ==
                                                    datetime.date.today().month) and (self.dtCurrentYMD.year == datetime.date.today().year):
                btn['state'] = 'active'
                btn['text'] = 'Today'
                btn['bg'] = 'red'
                blIsCurrentMonth = True
            else:
                if (self.dtCurrentYMD.month == datetime.date.today().month) and (self.dtCurrentYMD.year == datetime.date.today().year):
                    if i < datetime.date.today().day:
                        btn['text'] = '%d/%d' % (mm, i)
                        btn['bg'] = '#888888'
                        btn['state'] = 'disabled'
                    else:
                        btn['text'] = '%d/%d' % (mm, i)
                        btn['state'] = 'active'
                        btn['bg'] = 'white'
                else:
                    btn['text'] = '%d/%d' % (mm, i)
                    btn['bg'] = 'white'
                    btn['state'] = 'active'

        m_last_date = datetime.date(yyyy, mm, days_of_month)
        #count = 0
        for i in range(m_start_day + days_of_month, 6 * 7):
            btn = self.btnAlldays[i]
            btn['bg'] = 'lightgreen'
            btn['state'] = 'active'

            d = m_last_date + \
                datetime.timedelta(days=(i - m_start_day - days_of_month + 1))
            #d = m_last_date + datetime.timedelta(days=(++count))
            btn['text'] = '%d/%d' % (d.month, d.day)

        check_result = self.__is_show_next_month(
            self.dtCurrentYMD.year, self.dtCurrentYMD.month)

        if self.__is_show_next_month(self.dtCurrentYMD.year, self.dtCurrentYMD.month):
            self.btnNextMonth['state'] = 'active'
        else:
            self.btnNextMonth['state'] = 'disabled'

        if self.__is_show_pre_month(self.dtCurrentYMD.year, self.dtCurrentYMD.month):
            self.btnPreMonth['state'] = 'active'
        else:
            self.btnPreMonth['state'] = 'disabled'

        self.lblCurrentMonth['text'] = self.dtCurrentYMD.strftime(" %Y/%m ")
        return

    def __show_next_month(self):
        next_ymd = self.__get_next_ymd(
            self.dtCurrentYMD.year, self.dtCurrentYMD.month)
        self.dtCurrentYMD = next_ymd
        print('\nNow show next ym is:', next_ymd)
        self.__refresh_calendar1(next_ymd.year, next_ymd.month)
        # self.__refresh_calendar2(next_ymd.year,next_ymd.month)
        return

    def __show_pre_month(self):
        pre_ymd = self.__get_pre_ymd(
            self.dtCurrentYMD.year, self.dtCurrentYMD.month)
        self.dtCurrentYMD = pre_ymd
        print('\nNow show pre ym is:', pre_ymd)
        self.__refresh_calendar1(pre_ymd.year, pre_ymd.month)
        self.__refresh_calendar2(pre_ymd.year, pre_ymd.month)
        return

    def  __is_show_next_month(self, yyyy, mm):
        '判断输入年月的下个月是否还在 calendar_span 天数之内'

        next_ymd = self.__get_next_ymd(yyyy, mm)
        print('__is_show_next_month - %s' % next_ymd)

        # 判断下月按钮是否还能继续使用
        end_date = datetime.date.today() + datetime.timedelta(days=calendar_span)

        if (end_date.month >= next_ymd.month):
            blShowNext = True
        else:
            blShowNext = False

        print('Check %d/%d, next_ymd is %s, end_date is %s, check result is %d\n' %
              (yyyy, mm, next_ymd, end_date, blShowNext))

        return blShowNext
    def __is_show_pre_month(self, yyyy, mm):
        pre_ymd = self.__get_pre_ymd(yyyy, mm)
        blShowPre = True
        if pre_ymd.month == datetime.date.today().month - 1:
            blShowPre = False
        print('Check %d/%d, lest_ymd is %s, current month is %s, check result is %d\n' %
              (yyyy, mm, pre_ymd, datetime.date.today(), blShowPre))
        return blShowPre

    def __get_next_ymd(self, yyyy, mm):
        next_ymd = datetime.date.today()
        if(mm == 12):
            next_ymd = datetime.date(yyyy + 1, 1, 31)
        else:
            m_range = calendar.monthrange(yyyy, mm + 1)
            next_ymd = datetime.date(yyyy, mm + 1, m_range[1])
        return next_ymd

    def __get_pre_ymd(self, yyyy, mm):
        pre_ymd = datetime.date.today()
        if(mm == 1):
            m_range = datetime.date(yyyy - 1, 12, 31)
        else:
            m_range = calendar.monthrange(yyyy, mm - 1)
            pre_ymd = datetime.date(yyyy, mm - 1, m_range[1])
        return pre_ymd

    def __refresh_calendar2(self, yyyy, mm):
        all_events = read_all_expanded_events()

        m_range = calendar.monthrange(yyyy, mm)
        m_start_day = m_range[0]
        days_of_month = m_range[1]

        calendar_start_date = datetime.date(
            yyyy, mm, 1) - datetime.timedelta(days=m_start_day)

        diff = 6 * 7 - m_start_day - days_of_month
        day_delta = datetime.timedelta(days=diff)
        calendar_end_date = datetime.date(yyyy, mm, days_of_month) + day_delta
        print('DEBUG,-Show events from %s to %s' %
              (calendar_start_date, calendar_end_date))

        for e in all_events:
            d = datetime.date(e.fm.year, e.fm.month, e.fm.day)
            if(d >= calendar_start_date and d <= calendar_end_date):
                print('Fetch event date is %s' % d)
                pos = 0
                if(d.month == calendar_start_date.month)and(calendar_start_date != mm):
                    diff = datetime.date(yyyy, mm, 1) - d
                    pos = m_start_day - diff.days
                    print(
                        '0)Pick %d th button for pre month events id[%d]-[%d]' % (pos, e.id, e.subid))
                elif(d.month == calendar_end_date.month)and (calendar_end_date.month != mm):
                    pos = m_start_day + days_of_month + d.day - 1
                    print(
                        '2)Pick %d th button for next month events id[%d]-[%d]' % (pos, e.id, e.subid))
                else:
                    pos = m_start_day + d.day - 1
                    print(
                        '2)Pick %d th button for current month events id[%d]-[%d]' % (pos, e.id, e.subid))
                btn = self.btnAlldays[pos]
                short_name = ''
                if(len(e.name) > 5):
                    short_name = e.name[0:5] + '...'
                else:
                    short_name = e.name

                btn['text'] += '\n%s' % short_name
        return
