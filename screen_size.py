# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-6-9
# Time：21:20
import math


def screen_size():
    s = input("请输入屏幕尺寸（英寸）：")
    size = int(s) * 2.54
    ratio_a = int(input("请输入长边比例："))
    ratio_b = int(input("请输入短边比例："))
    ratio_A = round(math.sqrt(abs(size - math.pow(ratio_a * ratio_a / ratio_b, 2))),2)
    ratio_B = round(math.sqrt(abs(size - math.pow(ratio_a, 2))),2)
    print("长度：{0}英寸*2.54≈{1}厘米\n宽度：{2}英寸*2.54≈{3}厘米".format("%.2f"%(ratio_A / 2.54), ratio_A, "%.2f"%(ratio_B / 2.54), ratio_B))


screen_size()







#  python 格式化输出保留两位小数
#
# #方法1：
# print("%.2f" % 0.13333)
#
# #方法2
# print("{:.2}".format(0.13333))
#
# #方法3
# round(0.13333, 2)
