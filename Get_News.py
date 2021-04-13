import jieba
import wordcloud
import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.132 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    return resp.text

net = "https://tophub.today/c/news?p="
m = 1
Dic_net = {'知乎': "node-6", '微博': "node-1", '澎湃':"node-51", '百度':"node-2", '网易': "node-234",
         '搜狗': "node-38", '今日头条': "node-3608", '观察者': "node-4428", '新浪': "node-242",'百度今日': "node-3225",
           '新京报': "node-2410", '人民网': "node-2387", '腾讯': "node-8657", 'CCTV国际': "node-4445"}

List_word = ["如何", "为什么", "看待", "请问", "怎么办", "哪些", "这些", "有了","怎么","这么","多少","问题","宣布",
             "现在","最后","一天","什么","评价","这一","游戏","事情","哪个","道歉","地区","没有","这个","带来","影响",
             "几个","怎样","真的","假的","是不是","朋友","一起","喜欢","对于","号发","一种","几种","喊话","火爆","表演",
             "一朵","少女","细节","自己","还是","作出","可以","做出","卫视","什么样","一个","去世","不能","应该","不要"] #词汇屏蔽表

#词汇屏蔽判断函数
def Check_word(x):
    for i in range(0,len(List_word)):
        if List_word[i] == x :
            return 1
    return 0

def Get_news(dict):
    for index in Dic_net.keys():
        if dict == index:
            return Dic_net[index]

def Get_txt(x,y=1):
    try:
        url = get_html(net + str(y))
        soup = BeautifulSoup(url, 'html.parser')
        return soup.find("div", {"class": "cc-cd", "id": x}).find_all('span', class_='t')
    except AttributeError:
        y = y+1
        return Get_txt(x, y)


def Get_cloud(list):
    #list = Get_txt()
    with open('test.txt', 'w') as file:
        for i in range(0, len(list)):
            y = str(list[i])
            # print(jieba.__lcut(y))
            for j in range(0, len(jieba.__lcut(y[16:-7]))):
                if len(jieba.__lcut(y[16:-7])[j]) > 1 and Check_word(jieba.__lcut(y[16:-7])[j]) == 0:
                    file.write(jieba.__lcut(y[16:-7])[j] + " ")
            file.write("\n")

    with open('test.txt', 'r') as sentence:
        # print(type(sentence.read()))
        wc = wordcloud.WordCloud(font_path='STXINGKA.TTF', width=671, height=400, prefer_horizontal=0.8,max_words=50)
        wc.generate(sentence.read())
        wc.to_file("cloud.png")
