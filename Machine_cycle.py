# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-7-14
# Time：16:57

import time


def Printer(text, waittime=0.1):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(waittime)


def Programe_colse_time():
    tim = [5, 4, 3, 2, 1]
    for t in tim:
        print('\033[2K\rThe program will close in {} second' .format(t), end='', flush=True)
        time.sleep(1)
a=input('请输入：')
if a=='x':
    x=float(input('请输入震荡频率:'))
    s = 1 / x * 12
    Printer('ok,sir\n一个机器周期所需的时间:{}us={}ms={}s\n'.format(s,s/1000,s/1000000))
    Programe_colse_time()
elif a=='z':
    z=float(input('请输入需要的时间单位ms：'))
    zc=z*1/1000
    print('需要{}机器周期'.format(zc))
else:
    Printer('Sir, your input have problem')