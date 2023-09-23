# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-6-7
# Time：23:30
import tkinter as tk


Find_Name = ["朱晓敏", "张许梁", "王凯", "金皓哲", "汪洋", "赵保乐", "牛金玉", "刘森森", "王腾跃", "庞俊杰", "赵睿", "李士龙", "郭小轩", "袁健程", "宋亦陶", "岳尤",
             "黄洋", "周睿", "邢雯博", "陆佳杰", "杨猛", "林云松", "薛菡旻", "陈成", "张洪语", "李政伟", "邵杰", "姜晓峰", "马林", "韩飞扬", "华涛", "陈鑫豪",
             "薛斌", "冯王君", "吴宇晨", "张洁", "叶壮", "沈新尚", "李长军", "戴世杰"]

Find_ID = [2022059401, 2022059402, 2022059403, 2022059404, 2022059405, 2022059406, 2022059407, 2022059408,
           2022059409, 2022059410, 2022059411, 2022059412, 2022059413, 2022059414, 2022059415, 2022059416,
           2022059417, 2022059418, 2022059419, 2022059420, 2022059421, 2022059422, 2022059423, 2022059424,
           2022059425, 2022059426, 2022059427, 2022059428, 2022059429, 2022059430, 2022059431, 2022059432,
           2022059433, 2022059434, 2022059435, 2022059436, 2022059437, 2022059438, 2022059439, 2022059440]

Find_Dormitory = ["2B#106", "8A#106", "8A#114", "8A#105", "8A#105", "8A#104", "8A#107", "8A#104", "8A#107", "8A#118",
                  "8A#104", "8A#118", "2B#106", "8A#115", "8A#106", "8A#116", "8A#107", "8A#118", "8A#205", "8A#114",
                  "8A#117", "8A#118", "8A#115", "8A#205", "8A#104", "8A#115", "8A#105", "8A#106", "8A#114", "8A#117",
                  "8A#117", "8A#114", "8A#116", "8A#116", "8A#105", "8A#117", "8A#106", "8A#116", "8A#107", "8A#115"]

Find_Home = ["无锡市", "无锡市", "无锡市", "无锡市", "宜兴市", "徐州市", "徐州市", "徐州市", "徐州市", "徐州市", "徐州市", "徐州市", "徐州市", "徐州市", "常州市",
             "常州市", "常州市", "苏州市", "苏州市", "连云港", "连云港", "盐城市", "盐城市", "盐城市", "盐城市", "盐城市", "盐城市", "扬州市", "扬州市", "扬州市",
             "扬州市", "扬州市", "丹阳市", "丹阳市", "镇江市", "泰州市", "宿迁市", "宿迁市", "宿迁市", "宿迁市"]

# want=int(input("次数："))
enter = input("请输入查询依据(姓名：1 学号：2 学号后两位：3)\n条件为：")
def i():
    for i in range(int(input("请输入查询人数:"))):
        def id():
            if enter == "1":
                enter_name = input("请输入姓名：")
                index_Find_Name = Find_Name.index(enter_name)
                return index_Find_Name
            elif enter=="2":
                enter_id=int(input("请输入学号："))
                index_Find_id=Find_ID.index(enter_id)
                return index_Find_id
            elif enter=="3":
                enter_ne=input("请输入学号后两位：")
                index_Find_ne=Find_ID.index(int("20220594"+enter_ne))
                return index_Find_ne
            else:
                return
        id=id()
        index_Find_Name = Find_Name[int(id)]  # 姓名

        index_Find_ID = Find_ID[int(id)]  # 学号

        index_Find_Dormitory = Find_Dormitory[int(id)]  # 宿舍

        index_Find_Home = Find_Home[int(id)]  # 籍贯

        result = '{0}的信息为：''\n''姓名：{0}''\n''学号后两位：{3}''\n''学号：{1}''\n''宿舍号：{2}''\n''邮箱：{1}@czie.edu.cn''\n''籍贯：{4}'.format(
            index_Find_Name,
            index_Find_ID,
            index_Find_Dormitory,
            int(index_Find_ID - 2022059400),
            index_Find_Home)

        f = open('./1.txt', 'a')
        f.write(result+"\n")
        f.close()
        print("ok")


i()

# # UI界面
# root = tk.Tk()  # 创建窗口
# root.geometry('600x360')  # 窗口大小
# root.title('Fibonacci sequence')  # 窗口标题
# page = tk.Frame(root)  # 由root框架创建
# page.pack()
#
# # 输入框
# tk.Label(page).grid(row=0, column=0)
# tk.Label(page, font="黑体", text="项数").grid(row=1, column=1)
# needvalue = tk.StringVar()
# tk.Entry(page, textvariable=needvalue).grid(row=1, column=2)
#
#
# # 创建按钮
# def show_result():
#     v = int(needvalue.get())  # 从文本框获取值并转换为int类型
#     text="第{0}项的值为{1}".format(v,fx(v))
#     output.insert(0, text)
#
#
# tk.Button(page, font="黑体", text='查询', command=show_result,width=12).grid(row=2, column=2)
#
# # 输出结果
# tk.Label(page, font="黑体",text="结果").grid(row=2, column=1)
# output = tk.Listbox(root,width=35)
# output.pack()
#
# root.mainloop()