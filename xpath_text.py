import requests
import lxml.etree
url = 'https://book.douban.com/'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
headers = {}
headers['user-agent'] = user_agent

response = requests.get(url,headers=headers)
result = lxml.etree.HTML(response.text)
name = result.xpath('//*[@class="list-col list-col5 list-express slide-item"]//div[@class="title"]/a/text()')
author = result.xpath('//*[@class="list-col list-col5 list-express slide-item"]//div[@class="author"]/text()')
# 替换空格
new_lst = [s.replace('\n                ', '') for s in author]
new_author = [s.replace('\n              ', '') for s in new_lst]

# print(name)
# print(new_author)

# //*[@class="subject-list-list"]//*[@class="drc-subject-info-title-text"]/text()

mylist ={}

mylist['标题'] = name
mylist['作者'] = new_author
columns_name =['标题名称','作者']
import pandas as pd
book1 =pd.DataFrame(mylist)
# book1 =pd.DataFrame(columns = columns_name,data = name)
book1.to_csv('./book2.csv',encoding ='utf-8')
print(book1)

