'''
Author: ASyo
Date: 2023-05-10 20:20:58
LastEditTime: 2023-07-06 14:28:07
'''
import time
import keyboard

def Printer(text, waittime=0.03):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(waittime)


def Programe_colse():
    Printer('If you want to close this program, please press the q key')
    while True:
        if keyboard.read_key() == "q":
            break


