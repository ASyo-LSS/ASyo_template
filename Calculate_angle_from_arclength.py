'''
Author: ASyo
Date: 2023-05-10 20:20:58
LastEditTime: 2023-07-06 14:28:07
'''
import time


def Printer(text, waittime=0.03):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(waittime)


def Programe_colse_time():
    for t in range(10,0,-1):
        print('\033[2K\rThe program will close in {} second' .format(t),end='')
        time.sleep(1)


def arc_length():
    Printer('\nPlease input arc length:')
    l = float(input())
    Printer('Please input radius:')
    r = float(input())
    a = l / r
    n = a * 57.3
    Printer('Calculating, please wait, please give me one second')
    time.sleep(1)
    Printer('\n\nOk,sir\nThe Central angle is: {0}°\n\n'.format(n))
    Programe_colse_time()
    # time.sleep(5)  # 等待5秒
Printer('Hi,nice to meet you.\nThis Programe is calcculate angle frome arc length.\nNow Please enter the necessary parameters according to the prompts\n')
arc_length()

