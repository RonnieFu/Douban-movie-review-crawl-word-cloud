# encoding = gbk

import requests
import pandas as pd
import re
import time
import csv
from bs4 import BeautifulSoup
import os
from urllib import request
# #outputfile name
# output_filename = 'douban_movie_xiaohonghua.csv'
#
# # url请求文件头
# header = {'Content-Type': 'text/html; charset=utf-8',
#           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# # 登录cookies
# Cookie = {
#     'Cookie': 'bid=T54NrOIukao; douban-fav-remind=1; gr_user_id=00c5b72c-804c-442b-8049-0ea9f30ac738; _vwo_uuid_v2=D51E1BF67FB014C20B0F2939563E43F4E|ce1c24487b1f7b4178eddd3620b0d410; __gads=ID=0fbe250e94a7533d-22f18ad6f5c40037:T=1606792955:RT=1606792955:R:S=ALNI_MbH9DRfj9pl6GCJ31AR_FPtnEpvHQ; viewed="10769749_2314275"; ll="118267"; ap_v=0,6.0; __utmz=30149280.1609913918.26.26.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utma=30149280.284457910.1592972128.1609598478.1609913918.26; dbcl2="229867810:+IPucCNAsjM"; ck=M-_w; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22986; __utmb=30149280.9.10.1609913918'
# }
# # 构造请求网址
# url_1 = "https://movie.douban.com/subject/35096844/comments?start="
# url_2 = "&limit=20&sort=new_score&status=P"
# # 循环抓取多页，循环变量start,0,20,40...

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
