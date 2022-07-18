# coding=utf8
import os
import xlwt
import re
import xlsxwriter

path = '/Users/bytedance/Documents/年报/上交所-年报/转TXT处理'
files = os.listdir(path)
txtList = [f for f in files if f.endswith(('.txt'))]
print(txtList)

for li in txtList:
    filepath = path + '/' + li
    print(filepath)
    with open(filepath, 'r+') as fd:
        lines = fd.readlines()
        for line in lines:
            print(line)
            strlist1 = line.replace('\n', '')
            strlist2 = strlist1.replace('，', '\r\n')
            strlist3 = strlist2.replace('。', '\r\n')
            strlist4 = strlist3.replace('  ', '\r\n')
            strlist5 = strlist4.replace('、', '\r\n')
            strlist6 = strlist5.replace('：', '\r\n')
            strlist7 = strlist6.replace('；', '\r\n')
            strlist8 = strlist7.replace(' ', '\r\n')
        # print(strlist2)
            for value in strlist8:
                print(value)
                file1 = '/Users/bytedance/Documents/年报/上交所-年报/txt换行分割' + '/' + li
                with open(file1, "a") as f1:
                    f1.write(value)