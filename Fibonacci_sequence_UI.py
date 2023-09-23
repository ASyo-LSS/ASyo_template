# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-5-31
# Time：0:17
import tkinter as tk


# 处理公式
def fx(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        n = int(n)
        return fx(n - 1) + fx(n - 2)


# UI界面
root = tk.Tk()  # 创建窗口
root.geometry('600x360')  # 窗口大小
root.title('Fibonacci sequence')  # 窗口标题
page = tk.Frame(root)  # 由root框架创建
page.pack()

# 输入框
tk.Label(page).grid(row=0, column=0)
tk.Label(page, font="黑体", text="项数").grid(row=1, column=1)
needvalue = tk.StringVar()
tk.Entry(page, textvariable=needvalue).grid(row=1, column=2)


# 创建按钮
def show_result():
    v = int(needvalue.get())  # 从文本框获取值并转换为int类型
    text="第{0}项的值为{1}".format(v,fx(v))
    output.insert(0, text)


tk.Button(page, font="黑体", text='查询', command=show_result,width=12).grid(row=2, column=2)

# 输出结果
tk.Label(page, font="黑体",text="结果").grid(row=2, column=1)
output = tk.Listbox(root,width=35)
output.pack()

root.mainloop()
