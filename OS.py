'''
Author: ASyo
Date: 2023-06-23 15:53:09
LastEditTime: 2023-07-26 16:32:30
'''
# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-6-23
# Time：15:53
# import os
import os

qq=r'"E:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe"'
eudic=r'"E:\Software\Youdao\Dict\YoudaoDict.exe"'
snipase='D:/Download/Others/tool/Snipaste-2.7.3-Beta-x64/Snipaste.exe'
deskpin='E:/Software/Deskpins/deskpins.exe'
os.startfile(qq)
os.startfile(eudic)
os.startfile(snipase)
os.startfile(deskpin)
'''
import os

# 定义.exe文件路径
exe_file1 = qq
exe_file2 = eudic

# 打开第一个.exe文件
os.startfile(exe_file1)

# 打开第二个.exe文件
os.startfile(exe_file2)
'''
'''
import subprocess

# 定义要运行的exe文件列表
exe_list = [qq, eudic, snipase,deskpin]

# 运行每个exe文件
for exe in exe_list:
    subprocess.Popen(exe)
'''
'''
import multiprocessing

# 定义.exe文件路径
exe_file1 = qq
exe_file2 = eudic

# 定义打开.exe文件的函数
def open_exe_file(exe_file):
    subprocess.Popen(exe_file)

# 创建两个进程来打开.exe文件
process1 = multiprocessing.Process(target=open_exe_file, args=(exe_file1,))
process2 = multiprocessing.Process(target=open_exe_file, args=(exe_file2,))

# 启动进程
process1.start()
process2.start()

# 等待进程结束
process1.join()
process2.join()
'''