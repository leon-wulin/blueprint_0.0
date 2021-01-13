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
from data_class_event import data_class

fn_event_defination = 'fn_event_defination.csv'
fn_event_180days = 'fn_event_180days.csv'
calendar_span=180

def add_event_defination(e_obj):
    f = codecs.open(fn_event_defination, 'a+', 'utf-8')

    writer = csv.writer(f)
    data = class_to_rowdata(e_obj)
    print(data)
    writer.writerow(data)
    f.close()
    return

def class_to_rowdata(e_obj):

    data = []
    data.append(e_obj.id)
    data.append(e_obj.subid)
    data.append(e_obj.type)
    data.append(e_obj.name)
    data.append(e_obj.fm)
    data.append(e_obj.to)
    data.append(e_obj.remind)
    data.append(e_obj.every_day)
    data.append(e_obj.every_week_day)
    data.append(e_obj.week_day)
    data.append(e_obj.month_day)
    e_obj.modified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append(e_obj.modified)

    return data

def rowdata_to_class(row_data):
    e_obj = data_class()
    e_obj.id = int(row_data[0])
    e_obj.subid = int(row_data[1])
    e_obj.type = int(row_data[2])
    e_obj.name = row_data[3]
    e_obj.fm = datetime.datetime.strptime(row_data[4], "%Y-%m-%d %H:%M:%S")
    e_obj.to = datetime.datetime.strptime(row_data[5], "%Y-%m-%d %H:%M:%S")
    e_obj.remind = row_data[6]
    e_obj.every_day = int(row_data[7])
    e_obj.every_week_day = int(row_data[8])
    e_obj.week_day = row_data[9]
    e_obj.month_day = int(row_data[10])
    e_obj.modified = datetime.datetime.strptime(
        row_data[11], "%Y-%m-%d %H:%M:%S")
    return e_obj

def read_all_events_defination():
    f = codecs.open(fn_event_defination, 'r', 'utf-8')
    reader = csv.reader(f)
    all_events_obj = []
    for e in reader:
        e_obj = rowdata_to_class(e)
        all_events_obj.append(e_obj)

    print("DEBUG--All Read:")
    for e in all_events_obj:
        print('Obj id=[%d],name=%s,From=[%s],Type of form=[%s]' %
              (e.id, e.name, e.fm, type(e.fm)))
    return all_events_obj

def read_all_expanded_events():
    f = codecs.open(fn_event_180days, 'r', 'utf-8')
    reader = csv.reader(f)
    all_events_obj = []
    for e in reader:
        e_obj = rowdata_to_class(e)
        all_events_obj.append(e_obj)

    return all_events_obj

def generate_all_events(e_defination):
    print('debug')
    f = codecs.open(fn_event_180days, 'w+', 'utf-8')
    writer = csv.writer(f)
    for e_obj in e_defination:
        data = []
        if(e_obj.type == 0):
            data = class_to_rowdata(e_obj)
            writer.writerow(data)
        elif(e_obj.type == 1):
            if (e_obj.every_day > 0):
                print('every %d days preform once' % e_obj.every_day)
                expand_every_day(e_obj,writer)
            if(e_obj.month_day>0):
                print('every %d month day preform once' % e_obj.month_day)
                expand_every_month(e_obj,writer)
            if(e_obj.every_week_day>0):
                print('every %d week day preform once' % e_obj.every_week_day)
                expand_every_week_day(e_obj,writer,0)
            if(e_obj.week_day!='0000000'):
                print('%s week day preform once' % e_obj.week_day)
                expand_week_day(e_obj,writer)
    f.close()
    return

def expand_every_day(e_obj, writer):
    print('---------expand_every_day-----------')
    start_date = datetime.date.today()
    end_date = datetime.date.today() + datetime.timedelta(days=calendar_span)
    day_delta = datetime.timedelta(days=e_obj.every_day)

    event_date_from = datetime.date(e_obj.fm.year, e_obj.fm.month, e_obj.fm.day)

    count = 0

    while(event_date_from < end_date):
        e_obj.subid = count

        e_obj.fm += day_delta
        e_obj.to += day_delta

        data = class_to_rowdata(e_obj)
        writer.writerow(data)
        count += 1
        event_date_from += day_delta

    return count

def expand_every_month(e_obj,writer):
    start_date=datetime.date.today()
    defined_date=check_ymd(
    start_date.year,start_date.month,e_obj.month_day)
    print('befor:start date=[%s],defined date=[%s]'%(start_date,defined_date))

    if(datetime.date.today()>defined_date):
        if(datetime.date.today().month==12):
            start_date=check_ymd(datetime.date.today().year+1,
            1,
            e_obj.month_day)
        else:
            start_date=check_ymd(
            datetime.date.today().year,
            datetime.date.today().month+1,
            e_obj.month_day
            )
    else:
        start_date=check_ymd(
        datetime.date.today().year,
        datetime.date.today().month,
        e_obj.month_day
        )
    end_date=datetime.date.today()+datetime.timedelta(days=calendar_span)

    event_time_from=datetime.time(
    e_obj.fm.hour,e_obj.fm.minute,e_obj.fm.second)

    event_time_to=datetime.time(
    e_obj.to.hour,e_obj.to.minute,e_obj.to.second)

    current_date=start_date

    count=0

    while(current_date<=end_date):
        e_obj.subid=count

        e_obj.fm=datetime.datetime.combine(current_date,event_time_from)
        e_obj.to=datetime.datetime.combine(current_date,event_time_to)

        data=class_to_rowdata(e_obj)
        writer.writerow(data)
        count+=1
        if(current_date.month<12):
            dt=check_ymd(
            current_date.year,
            current_date.month+1,
            e_obj.month_day
            )
            current_date=dt
        else:
            dt=check_ymd(
            current_date.year+1,
            1,
            e_obj.month_day
            )
            current_date=dt
    return count

def expand_every_week_day(e_obj,writer,count_from):
    print('-------------expand_every_week_day----------')
    start_date= datetime.date.today()
    diff=datetime.date.today().weekday()-e_obj.every_week_day
    if(diff<0):
        start_date=datetime.date.today()+datetime.timedelta(days=(diff*-1))
    else:
        start_date=datetime.date.today()+datetime.timedelta(days=(7 - diff))

    end_date=datetime.date.today()+datetime.timedelta(days=calendar_span)
    print("before:today=[%s],start_date=[%s],end_date=[%s]"%
        (datetime.date.today(),start_date,end_date))
    event_time_from=datetime.time(
        e_obj.fm.hour, e_obj.fm.minute,e_obj.fm.second)
    event_time_to=datetime.time(
        e_obj.to.hour, e_obj.to.minute,e_obj.to.second)
    current_date=start_date
    count=count_from
    while(current_date<=end_date):
        e_obj.subid=count

        e_obj.fm=datetime.datetime.combine(current_date,event_time_from)
        e_obj.to=datetime.datetime.combine(current_date,event_time_to)

        data=class_to_rowdata(e_obj)
        writer.writerow(data)
        count+=1
        current_date+=datetime.timedelta(days=7)
    return (count - count_from)

def expand_week_day(e_obj,writer):
    start_date= datetime.date.today()
    end_date=datetime.date.today()+datetime.timedelta(days=calendar_span)

    week_days=e_obj.week_day
    expanded=0
    for i in range(7):
        p1=i
        p2=p1+1
        if(p2<=len(week_days)):
            c=week_days[p1:p2]
            print(c)
            if(c=='1'):
                print('Debug-begin %d time'%i)
                new_e_obj=copy.deepcopy(e_obj)
                new_e_obj.every_week_day=i
                count=expand_every_week_day(new_e_obj,writer,expanded)
                expanded +=count
                print("Debug - expand=",expanded)
    return expanded

def check_ymd(yyyy,mm,dd):
    m_range=calendar.monthrange(yyyy,mm)

    last_day=m_range[1]

    if (dd<=last_day):
        checked_date=datetime.date(yyyy,mm,dd)
    else:
        checked_date=datetime.date(yyyy,mm,last_day)
    return checked_date

def read_period_events(fm,to):
    f = codecs.open(fn_event_defination, 'r', 'utf-8')
    reader = csv.reader(f)
    all_events_obj = []
    for e in reader:
        e_obj = rowdata_to_class(e)
        if e_obj.fm>=fm and e_obj.fm<=to:
            all_events_obj.append(e_obj)
    return all_events_obj

def sort_events(events_list):
    '对接收到的事件列表按开始时间进行升序排列'

    n = len(events_list) - 1
    while n > 0:
        for i in range(0, n):
            if events_list[i].fm > events_list[i + 1].fm:
                events_list[i], events_list[i + 1] = events_list[i + 1], events_list[i]
        n -= 1
    return
