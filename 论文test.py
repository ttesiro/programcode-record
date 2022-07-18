
# coding=utf8
import os
import xlwt
import re
import xlsxwriter

path = '/Users/bytedance/Downloads/CNKI-20220128180618819.txt'

# files = os.listdir(path)
# txtList = [f for f in files if f.endswith(('txt'))]
# print(txtList)

workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
#workbook = xlsxwriter.Workbook('/Users/bytedance/Documents/年报/Output.xls')
sheet = workbook.add_sheet('Output', cell_overwrite_ok=True)
#sheet = workbook.add_worksheet('Output')
sheet.write(0, 0, '作者')
sheet.write(0, 1, '年份')
sheet.write(0, 2, '标题')
sheet.write(0, 3, '期刊')
sheet.write(0, 4, '摘要')
i = 1
j = 1
k = 1
o = 1
p = 1
with open(path, 'r+', encoding='UTF-8', errors='ignore') as fd:
    for text in fd.readlines():
        if "%A" in text:
            print(i)
            sheet.write(i, 0, text)  # 往表格里写入Y坐标
            i = i + 1
        if "%D" in text:
            j = max(i-1, j)
            print("j:",j)
            sheet.write(j, 1, text)  # 往表格里写入Y坐标
            j = j + 1
        if "%T" in text:
            k = max(i-1, k)
            #k = max(i, j, k)
            sheet.write(k, 2, text)  # 往表格里写入Y坐标
            k = k + 1
        if "%J" in text:
            o = max(i-1, o)
            sheet.write(o, 3, text)  # 往表格里写入Y坐标
            o = o + 1

        if "%X" in text:
            p = max(i-1, p)
            sheet.write(p, 4, text)  # 往表格里写入Y坐标
            p = p + 1

n = max(i, j, k, o, p)
i = max(i, j, k, o, p)
j = max(i, j, k, o, p)
k = max(i, j, k, o, p)
o = max(i, j, k, o, p)
o = max(i, j, k, o, p)
# 最后，将以上操作保存到指定的Excel文件中
workbook.save('/Users/bytedance/Downloads/output0128.xls')



