# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-8-15
# Time：20:29
# 输入你的句子
import re
import sys

def is_chinese(s):
    return re.match("[\u4e00-\u9fa5]+$", s) is not None

def Symbol(s):
    chinese_punctuation = r"，。!  ？；：“”‘’【】（）《》 、 -"
    sentence = s
    result = ""
    for char in sentence:
        if char in chinese_punctuation:  # 检查是否为标点符号
            result += char
        elif is_chinese(char):
            result +=  char + "！"
        else:
            result += '\n'
    return result

# 获取歌词
lines = []
while True:
    text = sys.stdin.readline().strip()
    if text == "x":
        break
    lines.append(text)
# 格式化数据
linex=''
for line in lines:
    linex+=line+'\n'
print(Symbol(linex))
