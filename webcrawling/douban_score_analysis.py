import pandas as pd
from collections import Counter

#读取csv文件
def score_analysis(output_file_name):
    df = pd.read_csv(output_file_name)

    #统计打分数量
    star_list = list(df['star'].values)
    num_count = Counter(star_list)
    #显示热评种不同分值的评论数量
    print("=================================分数统计==========================================")
    print(num_count)

    #分组求平均
    grouped = df.groupby('star').describe().reset_index()
    star = grouped['star'].values.tolist()
    print(star)

    #根据用户打分的分组，对每组的情感值求平均
    sentiment_average = df.groupby('star')['sentiment_score'].mean()
    sentiment_scores = sentiment_average.values
    print(sentiment_scores)
    print("===================================================================================")
