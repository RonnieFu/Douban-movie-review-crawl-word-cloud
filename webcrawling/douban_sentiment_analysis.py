# encoding=gbk
import pandas as pd
from snownlp import SnowNLP

def sentiment_analysis(output_filename):
    df_1 = pd.read_csv(output_filename, header=None, usecols=[1, 2, 3, 4, 5])
    df_1.columns = ['uname', 'comment', 'star', 'title', 'support']
    # 填补空值
    df_1['comment'].fillna(" ",inplace=True)
    df_1['star'] = df_1['star'].astype(str)
    df_1['star'] = df_1['star'].str.replace("allstar", "")
    df_1['star'] = df_1['star'].str.replace("0", "")
    df_1['star'] = df_1['star'].apply(lambda x: 3 if len(x) > 1 else x)
    # df_1['star']=df_1['star'].str.replace("33","3")
    df_1['star'].fillna(3, inplace=True)
    # 读抓取的csv文件，标题在第三列，序号为2
    df = pd.read_csv(output_filename, header=None, usecols=[2])

    # 将dataframe转换为List
    contents = df.values.tolist()
    # 数据长度

    # 定义空列表存储情感分值
    score = []
    for content in contents:
        try:
            s = SnowNLP(content[0])
            # print(s.summary())
            score.append(s.sentiments)
        except:
            #TODO 检查错误要把这里加一个输出
            #print("")
            #自动填补为
            score.append(0.5)
    data2 = pd.DataFrame(score)
    # data2.to_csv('sentiment.csv',header=False,index=False,mode='a+')

    # 整理两个表格
    df_1['sentiment_score'] = data2

    df_1.to_csv(output_filename, index=False)
