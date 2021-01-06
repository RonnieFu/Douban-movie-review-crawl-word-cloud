from wordcloud import WordCloud
import jieba
import numpy as np
import PIL.Image as Image
import pandas as pd


def chinese_jieba(text):
    wordlist_jieba = jieba.cut(text)
    space_wordlist = " ".join([str(i) for i in wordlist_jieba])
    return space_wordlist

def WORDCLOAD(output_filename,wordcloud_name,stop_word,star):
    stop_words = pd.read_csv(stop_word, encoding='utf-8')
    # 读取csv文件
    df = pd.read_csv(output_filename)
    comment_list = df['comment'].values.tolist()
    star_list = list(df['star'].values)

    text = ""
    for jj in range(len(comment_list)):
        if star_list[jj] in star:
            text = text + chinese_jieba(comment_list[jj])

    # 调用PIL中的open方法，读取图片文件，通过numpy中的array方法生成数组
    mask_pic = np.array(Image.open("background_love.jpg"))
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/STZHONGS.TTF",
                            mask=mask_pic,
                          background_color='white',
                          max_font_size=150,
                          max_words=200,
                          stopwords={i for i in set(stop_words.iloc[:,0])},
                          ).generate(text)
    image = wordcloud.to_image()
    #wordcloud.to_file('ciyun.png')
    wordcloud.to_file(wordcloud_name)
    image.show()