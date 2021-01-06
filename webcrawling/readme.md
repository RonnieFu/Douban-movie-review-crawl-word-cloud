## 豆瓣电影评论爬取+情感分析+词云

注意未登录的豆瓣账号(不填写Cookie，只能爬取200条评论，登陆后填写可以爬取500条)

运行该项目需要调整好main.py中的参数,直接运行即可

### 主要修改

url_1中电影号修改为对应豆瓣中的电影号

![image-20210106194656245](https://i.loli.net/2021/01/06/icQvZnNy1zoHAdT.png)

加到应代码的url的subject后面数字位置即可

```python
url_1 = "https://movie.douban.com/subject/27073752/comments?start="
```