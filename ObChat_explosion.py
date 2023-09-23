# 本程序功能以定义的次数执行消息轰炸，仅用于学习交流
from pynput.keyboard import Key, Controller
import time

# import pyperclip

keyboard = Controller()
messages =input('Name:')
times = int(input('次数：'))

print("OK, Please wait")
time.sleep(0.1)
for i in range(3):
    print("need wait: %d" % (3 - i))
    time.sleep(1)
for i in range(times):
    # s = '第' + str(i + 1) + '次'
    # keyboard.type(s)
    st=str(i + 1) + '次：'
    keyboard.type(messages)
    keyboard.type(st)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)
print("Task over !")
