#!/usr/bin/env python3
import pyttsx3
import colorama
import sys
import time
import os
from time import sleep
from threading import Thread

colorama.init()
print(colorama.Style.BRIGHT, end="")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[int(sys.argv[2])].id)


def play_sound(mytext):
    engine.say(mytext)
    engine.runAndWait()


def write_to_screen(mytext):
    if len(mytext.strip()) != 0 and mytext[0] == '(':
        print(colorama.Fore.RED, mytext, end=" ")
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '-' :
        print(colorama.Fore.GREEN, mytext, end=" ")
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '*' :
        print(colorama.Fore.MAGENTA, mytext, end=" ")
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '~' :
        print(colorama.Fore.BLUE, mytext, end=" ")
    elif len(mytext.strip()) != 0 and mytext.lstrip()[0] == '+' :
        print(colorama.Fore.CYAN, mytext, end=" ")
    else:
        print(mytext, end="")
    
    print(colorama.Fore.WHITE, "", end="")


now = time.time()


def sprint(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(1./115)


file1 = open(str(sys.argv[1]), 'r')
Lines = file1.readlines()
for line in Lines:
    Thread(target=write_to_screen(line)).start()
    Thread(target=play_sound(line.strip())).start()
file1.close()

later = time.time()
difference = int(later - now)
print("time: ", difference, "seconds")
