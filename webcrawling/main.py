import pandas as pd
from douban_wordcloud import *
from douban_sentiment_analysis import *
from douban_score_analysis import *
from douban_movie_comment import *
def play(output_filename,header,Cookie,url_1,url_2,sleep_time,wordcloud_name,stop_word,star):
    crawl(output_filename,header,Cookie,url_1,url_2,sleep_time)
    sentiment_analysis(output_filename)
    score_analysis(output_filename)
    WORDCLOAD(output_filename,wordcloud_name,stop_word,star)

if __name__=='__main__':
    #输出文件名
    output_filename = 'douban_movie_wonder_woman_1-5.csv'

    # url请求文件头,User-Agent要改为自己登录后的
    header = {'Content-Type': 'text/html; charset=utf-8',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    # 登录cookies,自己填写登录豆瓣后的cookie
    Cookie={

    }
    # Cookie = {
    #     'Cookie': 'bid=T54NrOIukao; douban-fav-remind=1; gr_user_id=00c5b72c-804c-442b-8049-0ea9f30ac738; _vwo_uuid_v2=D51E1BF67FB014C20B0F2939563E43F4E|ce1c24487b1f7b4178eddd3620b0d410; __gads=ID=0fbe250e94a7533d-22f18ad6f5c40037:T=1606792955:RT=1606792955:R:S=ALNI_MbH9DRfj9pl6GCJ31AR_FPtnEpvHQ; viewed="10769749_2314275"; ll="118267"; ap_v=0,6.0; __utmz=30149280.1609913918.26.26.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utma=30149280.284457910.1592972128.1609598478.1609913918.26; dbcl2="229867810:+IPucCNAsjM"; ck=M-_w; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22986; __utmb=30149280.9.10.1609913918'
    # }
    # 构造请求网址
    url_1 = "https://movie.douban.com/subject/27073752/comments?start="
    url_2 = "&limit=20&sort=new_score&status=P"
    #睡眠时间
    sleep_time =2
    #词云文件名
    wordcloud_name = 'ciyun.png'
    #停用词存放地址
    stop_word='hit_stopwords.txt'
    #生成词云要使用的评分,一共是1-5
    star=[5]

    #词云,对应8个参数为输出文件名，Cookie,url第一部分，url第二部分,睡眠时间，输出词云文件名，要看是哪些评星的词云
    play(output_filename,header,Cookie,url_1,url_2,sleep_time,wordcloud_name,stop_word,star)