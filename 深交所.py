import pandas as pd
import requests
import random
import time
import os

rawdata = pd.read_excel(r'/Users/bytedance/Documents/年报/深圳证券交易所-搜索页面-采集的数据-后羿采集器1.xlsx', sheet_name=0)


def get_data(iloc):
    rawdata['year'] = rawdata['rep_period'].dt.year
    rawdata['security_name'] = rawdata['security_name'].astype(str)
    firm = rawdata.at[iloc, 'security_name'].replace("*", "")  # 去掉*ST的*号，文件命名不含特殊符号
    #code = rawdata.at[iloc, 'security_code']
    year = rawdata.at[iloc, 'year']
    pdf_url = rawdata.at[iloc, 'rep_link']
    return firm, year, pdf_url


def get_filepath(firm, year):
    file_path = '/Users/bytedance/Documents/年报/深交所-年报'
    file_name = "{}-{}年年度报告.pdf".format(firm, year)
    file_full_name = os.path.join(file_path, file_name)
    return file_full_name


def download_pdf(url, file_full_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}
    res = requests.get(url, headers=headers)
    with open(file_full_name, "wb") as fp:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)


for iloc in range(rawdata.shape[0]):
    firm, year, pdf_url = get_data(iloc)
    print("开始下载{}，{}年报".format(firm, year))
    file_full_name = get_filepath(firm, year)
    download_pdf(pdf_url, file_full_name)
    time.sleep(random.uniform(3, 4))
    print("===========下载完成==========")
