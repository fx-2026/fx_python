import requests
#get 和 post
from bs4 import BeautifulSoup as bs

# 示例HTML
# 创建BeautifulSoup对象
# soup = BeautifulSoup(content, 'html.parser')  # 使用Python内置解析器
# 或使用lxml解析器（推荐）


def getdaoban(urls):
    # 自定义头部
    user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    headers={}
    headers['user-agent'] =user_agent

    #抓取网页
    response = requests.get(urls,headers=headers)


    #解析网页
    bs_info = bs(response.text, 'html.parser')
    #找到标签的内容
    result =bs_info.find_all('div',attrs={'class':"pl2"})[0].find_all('a')

    titles=[]
    imgs =[]

    #用find_all找到标签内容
    #最后get 标题
    for results in bs_info.find_all('div',attrs={'class':"pl2"}):
        for result in results.find_all('a'):
            titles.append(result.get('title'))
            print(result.get('title'))
  
    # print(titles)

    # for i in bs_info.find_all('tr',attrs={'class':"item"}):
    #     for j in i.find_all('a'):
    #         for x in j.find_all('img'):
    #             img =x.get('src')

j = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(11))#地址

from time import sleep
for url in j:
    print(getdaoban(url))
    sleep(30)