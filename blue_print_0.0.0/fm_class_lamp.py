# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : Leon
# created:  2020.7

# Description:
#   Blueprint 技术验证用
#   保存、读取文件的模块
# ------------------------(max to 80 columns)-----------------------------------

import wave
import sys
import os
import codecs
import random
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from mod_event import*
import pyaudio

class MyFrameLamp:

    wave_file_path=''
    def __init__(self,pwin,title,grid_x,grid_y):
        self.pwin=pwin
        self.wave_file_path=os.getcwd()+'\\alarm_sound\\Alarm01.wav'
        lbfLamp=ttk.Labelframe(pwin,text=title,width=250,height=20)
        lbfLamp.grid(row=grid_x,column=grid_y,columnspan=7,padx=5,pady=5,stick=tk.W)
        self.lblEvents=tk.Label(
        lbfLamp,text='Alerting events...',relief='raised',fg='red')
        self.lblEvents.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
        return

    def refresh_events(self):
        start_dt=datetime.datetime.now()
        end_dt=datetime.datetime.now()+datetime.timedelta(minutes=30)
        print("MyFrameLamp: Refresh period [%s]-[%s]"%(start_dt,end_dt))
        alert_event= read_period_events(start_dt,end_dt)
        ss='No alerting events at present.'
        if len(alert_event)>0:
            ss=''
            for e in alert_event:

                s='%s %s to %s \n'%(e.name,e.fm,e.to)
                ss+=s
        self.lblEvents['text']=ss
        self.__play_alarm()
        return

    def __play_alarm(self):
        '播放指定文件名的提醒音乐'
        
        chunk = 1024
        wf = wave.open(self.wave_file_path, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(chunk)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()

       
        return
