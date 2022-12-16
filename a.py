import audioop

import time
from math import log10
from threading import *

from threading import Thread
import keyboard
import sys

from pynput.mouse import Button, Controller


import pyaudio

from playsound import playsound
from tkinter import ttk
import tkinter as daş
from tkinter import *
global clearthis
global ılk_pencere

kapa = 0


average = [0, 0, 0, 0, 0, 0, 0, 0, 0]
average_sum = 0
i = 0
clearthis = 0
p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']

bot = 0

rms = 0
db = 0
global var
var = 0
file1 = open("oku.txt", "r+")


def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue


# def progress_bar(current_value, total):
    increments = 100
    percentual = ((current_value / total) * 100)
    i = int(percentual // (100 / increments))
    text = "\r[{0: <{1}}] {2}%    ".format(
        '=' * i, increments, int(percentual))
    print(text, end="\t" if percentual == 100 else "")


stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)
stream.start_stream()
aq = 0
seviye = 80
on = TRUE


def doSomething():
    global kapa
    kapa = 1


def setbot(a):
    if (int(a) < 1):
        return
    global bot
    bot = int(a)


oh = 0


def getoh():
    oh = 0
    return oh


def setoh():
    oh = 1
    return oh


global yok
yok = True


def sok():

    global on
    if (on == TRUE):
        window = Tk()
        window.title("mantıklı")
        window.geometry("150x300")

        ##########
        sus = Toplevel()
        sus.title("1")
        sus.geometry("300x8")
        sus.overrideredirect(True)
        suspb = ttk.Progressbar(sus, mode='determinate',orient=HORIZONTAL, length=300)
        sus.wm_attributes("-topmost", 1)
        suspb.place(x=0, y=0)
        suspb.pack()

        on = False
        global aq
        s1 = Scale(window, variable=IntVar(), from_=101, to=1,orient=VERTICAL, sliderlength=10, showvalue=1, length=190)
        s1.set(getak())

        s1.place(x=0, y=20)

        pb = ttk.Progressbar(window, mode='determinate',orient=VERTICAL, length=191)
        pb.place(x=50, y=22)
        sa = Label(window, text="Soundmeter")
        sa.place(x=75, y=40)
        asa = Label(window, text="with gui")
        asa.place(x=75, y=60)
        tasa = Label(window, text="Çarpan sayısı")
        tasa.place(x=3, y=230)
        kasa = Entry(window, width=7)
        file2 = open("oku.txt", "r+")

        cuc = file2.read().split(" ")
        tok = (int(cuc[1]))
        file2.close()
        kasa.insert(END, tok)

        kasa.place(x=80, y=230)
        b1 = daş.Button(window, text="Değiştir", height=1,width=7, command=setbot(kasa.get()))
        b1.place(x=80, y=255)

        var = daş.IntVar()
        window.protocol('WM_DELETE_WINDOW', doSomething)
        pastırma = Checkbutton(window, text="mini_aç",variable=var,onvalue=1,offvalue=0,height=5,width=5)
        var.set(1)
        pastırma.place(x=80, y=120)
        window.lift()
        global yok
        t2 = Thread(target=çık).start()

        ############################################
        while (True):

            setak(s1.get())
            pb['value'] = love
            suspb['value'] = love
            window.update()
            global kapa
            baş = kasa.get()
            a = ''
            for i in range(len(baş)):
                if (baş[i].isdigit()):
                    a = a+baş[i]
            if (a != ""):
                if (int(a) >= 0):
                    setbot(a)
            if (kapa == 1):
                exit()
            if (var.get() == 1 and yok == True):
                sus.overrideredirect(True)
                sus.update()
                sus.lift()
                sus.deiconify()
            else:
                sus.lift()
                sus.withdraw()


def çık():
    global yok

    while {True}:
        tuş = keyboard.read_key()
        if (tuş == "home"):
            yok = not yok
            time.sleep(1)
        if (kapa == 1):
            exit()


def getak():
    return seviye


def setak(ol):
    global seviye
    time.sleep(0.1)
    if (ol >= 101 or ol <= 0):
        return
    seviye = ol


mantık = file1.read()
mantık = mantık.split(" ")[0]
setak(int(mantık))
file1.close()
win12 = Thread(target=sok).start()
while stream.is_active():
    if rms != 0.0:
        db = bot * log10(rms)

        #print(f"RMS: {rms} DB: {db}")
        average[i] = db
        i = i+1
        clearthis = clearthis+1
        if clearthis > 300:

            file1 = open("oku.txt", "w")  # write mode
            basL = bot
            L = getak()
            L = str(L)
            L = L+" "+str(basL)
            L = str(L)
            file1.writelines(L)
            file1.close()
            clearthis = 0

        if i == 9:
            i = 0
        for x in range(0, 9):
            average_sum = average_sum+average[x]
        average_sum = average_sum/10
        love = 100-average_sum*(-1)

        ak = getak()
        #progress_bar(love, 100)
        # print(seviye)
        if ak < love:
            playsound('a.wav')
            # Beep at 1000 Hz for 100 ms
        if (kapa == 1):
            break

    time.sleep(0.001)
