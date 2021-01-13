# -*- coding: UTF-8 -*-
import pyaudio
import wave
import sys
import os


def play_alarm(wav_file):
    '播放指定文件名的提醒音乐'
    chunk = 1024
    wf = wave.open(wav_file, 'rb')
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

for i in range(1,11):

    fn =os.getcwd()+'\\alarm_sound\\Alarm%0.2d.wav'%i
    print(fn)
    print('playing %d wav sound...'%i)
    play_alarm(fn)
