'''
Author: ASyo
Date: 2023-07-08 00:44:00
LastEditTime: 2023-07-08 14:30:53
'''
# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-7-8
# Time：0:44
import base64
i = open('D:\Download\Pictures\Godfather.png','rb') # rb二进制方式打开文件用于只读
Base64 = base64.b64encode(i.read()) #读取文件内容，转换为base64编码
i.close()
print(r'data:image/png;base64{}'.format(Base64))