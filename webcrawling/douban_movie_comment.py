# encoding = gbk

import requests
import pandas as pd
import re
import time
import csv
from bs4 import BeautifulSoup
import os
from urllib import request

def crawl(output_filename,header,Cookie,url_1,url_2,sleep_time):
    i = 0
    while True:
        # 拼接url
        url = f"{url_1}{str(i * 20)}{url_2}"
        print(url)
        try:
            #request请求
            html = requests.get(url,headers=header,cookies=Cookie)
            #beautifulsoup
            soup = BeautifulSoup(html.content,'lxml')
            #评论时间
            comment_time_list = soup.find_all('span',attrs={'class':'comment-time'})
            #设置循环终止变量
            if len(comment_time_list)==0:
                break
            #评论用户名
            use_name_list = soup.find_all('span',attrs={'class':'comment-info'})
            #评论文本
            comment_list = soup.find_all('span',attrs={'class':'short'})
            #评分
            rating_list = soup.find_all('span',attrs={'class':re.compile(r"allstar(\s\w+)?")})
            #支持
            support_list = soup.find_all('span',attrs={'class':'votes vote-count'})
            for jj in range(len(comment_time_list)):
                data1 = [(comment_time_list[jj].string,
                          use_name_list[jj].a.string,
                          comment_list[jj].string,
                          rating_list[jj].get('class')[0],
                          rating_list[jj].get('title'),
                          support_list[jj].string)]
                data2 = pd.DataFrame(data1)
                data2.to_csv(output_filename,header=False,index=False,mode='a+')
        except Exception as E:
            print('something is wrong')
        print('page '+str(i+1)+' is done')
        i+=1
        time.sleep(sleep_time)
