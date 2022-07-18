# coding=utf8
import os
import xlwt
import re
import xlsxwriter
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = workbook.add_sheet('Output', cell_overwrite_ok=True)

sheet.write(0, 0, '名称')
sheet.write(0, 1, '股东')
sheet.write(0, 2, '员工')
sheet.write(0, 3, '供应商')
sheet.write(0, 4, '客户')
sheet.write(0, 5, '债权人')
sheet.write(0, 6, '公共关系')
sheet.write(0, 7, '社会责任建设')
sheet.write(0, 8, '安全生产')
sheet.write(0, 9, '环境')
n = 1
i = 1
j = 1
k = 1
o = 1
p = 1
q = 1
r = 1
s = 1
t = 1

with open('/Users/bytedance/Documents/年报/深交所newtxt/txt文件韵达股份：2019年社会责任报告-2020年年度报告.txt', 'r+') as fd:
    #sheet.write(n, 0, li[0:-1])
    for text in fd.readlines():
        if "股东" in text or "股东大会" in text or "投资者" in text or "公告" in text or "接待" in text or "董事会" in text or "监事会" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(i, 1, text)  # 往表格里写入Y坐标
                i = i + 1
        if "员工" in text or "培训" in text or "组织" in text or "职工" in text or "发放" in text or "人员" in text or "慰问" in text or "覆盖率" in text or "健康" in text or "劳动合同" in text or "体检" in text or "职业" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(j, 2, text)  # 往表格里写入Y坐标
                j = j + 1
        if "供应商" in text or "采购" in text or "合作" in text or "质量" in text or "认证" in text or "评估" in text or "审核" in text or "合同" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(k, 3, text)  # 往表格里写入Y坐标
                k = k + 1
        if "客户" in text or "质量" in text or "服务" in text or "满意度" in text or "管理体系" in text or "认证" in text or "投诉" in text or "ISO" in text or "合格率" in text or "标准" in text or "顾客" in text or "用户" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(o, 4, text)  # 往表格里写入Y坐标
                o = o + 1
        if "投资者" in text or "利息" in text or "融资" in text or "银行" in text or "债权人" in text or "投资" in text or "债券" in text or "融资券" in text or "偿还" in text or "贷款" in text or "信用" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(p, 5, text)  # 往表格里写入Y坐标
                p = p + 1
        if "捐赠" in text or "扶贫" in text or "帮扶" in text or "捐款" in text or "公益" in text or "爱心" in text or "资助" in text or "基金会" in text or "教育" in text or "脱贫" in text or "帮助" in text or "志愿者" in text or "慈善" in text or "贫困" in text or "捐助" in text or "慰问" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(q, 6, text)  # 往表格里写入Y坐标
                q = q + 1
        if "社会" in text or "责任" in text or "履行" in text or "措施" in text or "改善" in text or "权益" in text or "保护" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(r, 7, text)  # 往表格里写入Y坐标
                r = r + 1
        if "安全" in text or "培训" in text or "生产" in text or "应急" in text or "事故" in text or "演练" in text or "整改" in text or "检查" in text or "隐患" in text or "排查" in text or "作业" in text or "职业病" in text or "健康" in text or "预案" in text or "消防" in text or "设备" in text or "体检" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(s, 8, text)  # 往表格里写入Y坐标
                s = s + 1
        if "排放" in text or "环保" in text or "环境" in text or "节能" in text or "节约" in text or "减排" in text or "能源" in text or "改造" in text or "处理" in text or "消耗" in text or "回收" in text or "认证" in text:
            if bool(re.search(r'\d', text)):
                sheet.write(t, 9, text)  # 往表格里写入Y坐标
                t = t + 1
n = max(i, j, k, o, p, q, r, s, t)
i = max(i, j, k, o, p, q, r, s, t)
j = max(i, j, k, o, p, q, r, s, t)
k = max(i, j, k, o, p, q, r, s, t)
o = max(i, j, k, o, p, q, r, s, t)
p = max(i, j, k, o, p, q, r, s, t)
q = max(i, j, k, o, p, q, r, s, t)
r = max(i, j, k, o, p, q, r, s, t)
s = max(i, j, k, o, p, q, r, s, t)
t = max(i, j, k, o, p, q, r, s, t)

# 最后，将以上操作保存到指定的Excel文件中
workbook.save('/Users/bytedance/Documents/年报/深交所-年报/Output.xls')



