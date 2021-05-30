#!/usr/bin/env python3
import os
import sys
import time
import pyttsx3
import textwrap
import colorama
from time import sleep
from datetime import date
from threading import Thread

now = time.time()

colorama.init()
print(colorama.Style.BRIGHT, end="")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[int(sys.argv[2])].id)

def sprint(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(1./120)

def play_sound(mytext):
    engine.say(mytext)
    engine.runAndWait()

def filltext(txt):  
  sprint(textwrap.fill(txt, 53) )

def write_to_screen(mytext):
    if len(mytext.strip()) != 0 and mytext[0] == '(':
        print(colorama.Fore.RED, end=" ")
        filltext(mytext)
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '-':
        print(colorama.Fore.GREEN, end=" ")
        filltext(mytext)
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '*':
        print(colorama.Fore.MAGENTA, end=" ")
        filltext(mytext)
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '~':
        print(colorama.Fore.BLUE, end=" ")
        filltext(mytext.replace('~', ''))
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '.':
        print(colorama.Fore.CYAN,  end="")
        filltext(mytext)
    else:
        filltext(mytext)

    print(colorama.Fore.WHITE, "")  


file1 = open(str(sys.argv[1]), 'r')
Lines = file1.readlines()
for line in Lines:
    Thread(target=write_to_screen(line)).start()
    Thread(target=play_sound(line.strip())).start()
    sleep(1./120)
file1.close()

later = time.time()
difference = int(later - now)
# print("time: ", difference, "seconds")

