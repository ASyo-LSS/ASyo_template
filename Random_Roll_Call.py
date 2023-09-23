import random
import tkinter as tk
import timeit
start=timeit.default_timer()
# 学生名单
students = ["朱晓敏","张许梁","王凯","金皓哲","汪洋","赵保乐","牛金玉","刘森森","王腾跃","庞俊杰","赵睿","李士龙","郭小轩","袁健程","宋亦陶","岳尤","黄洋","周睿","邢雯博","陆佳杰","杨猛","林云松","薛菡旻","陈成","张洪语","李政伟","邵杰","姜晓峰","马林","韩飞扬","华涛","陈鑫豪","薛斌","冯王君","吴宇晨","张洁","叶壮","沈新尚","李长军","戴世杰","朱先国","金烨","邵磊","俞雷","程浩文"]

# 随机选择一个学生
t = '幸运嘉宾\n'+random.choice(students)
# # 在窗口中显示结果
# print('你被点名了！')
# print('你选择了：', selected_student)


# 创建一个窗口
window = tk.Tk()
window.title('被点到的人')
# 创建一个标签
label = tk.Label(window, text=t, font=("微软雅黑", 100))
label.pack()
end=timeit.default_timer()
print(end-start)
# 进入主循环
window.mainloop()