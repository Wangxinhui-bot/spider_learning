#!/usr/bin/python
# coding: utf-8


import requests
from bs4 import BeautifulSoup
import re


# 丁香园的链接
link = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

# 伪装成浏览器
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

# 获取html文件
r = requests.get(link, headers = headers)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, "html.parser")

statistic = soup.find('script', attrs={'id': 'getListByCountryTypeService1'})


# 匹配省份
pattern1 = re.compile(r'"provinceShortName":"\w+')
result1 = pattern1.findall(str(statistic))
i=0
for word in result1:
    result1[i] = re.sub(r'"\w+":"',"",word)
    i+=1

def Name_get():
    return result1

# 匹配现存确诊
pattern2 = re.compile(r'"currentConfirmedCount":\d+')
result2 = pattern2.findall(str(statistic))
i=0
for word in result2:
    result2[i] = re.sub(r'"\w+":',"",word)
    i+=1

def current_get():
    return result2

# 匹配累计确诊
pattern3 = re.compile(r'"confirmedCount":\d+')
result3 = pattern3.findall(str(statistic))
i=0
for word in result3:
    result3[i] = re.sub(r'"\w+":',"",word)
    i+=1

def confirmed_get():
    return result3

# 匹配治愈
pattern4 = re.compile(r'"curedCount":\d+')
result4 = pattern4.findall(str(statistic))
i=0
for word in result4:
    result4[i] = re.sub(r'"\w+":',"",word)
    i+=1

def cure_get():
    return result4

# 匹配死亡
pattern5 = re.compile(r'"deadCount":\d+')
result5 = pattern5.findall(str(statistic))
i = 0
for word in result5:
    result5[i] = re.sub(r'"\w+":',"",word)
    i+=1
def death_get():
    return result5

"""
i = 0
for i in range(34): 
    print("{}地区 现存确诊{} 累计确诊{} 治愈{} 死亡{}".format(result1[i],result2[i],result3[i],result4[i],result5[i]))
"""

cure_rate = []
i = 0
for i in range(34):
    cure_rate.append(float(result4[i])/float(result3[i]))

province_rate = dict(zip(result1, cure_rate))
print(sorted(province_rate.items(), key = lambda kv:(kv[1], kv[0])))


