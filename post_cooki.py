import requests

#包头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
headers = {}
headers['user-agent'] = user_agent


#用session保存账号密码登录后的cookie
s = requests.Session()

url1 = 'https://accounts.douban.com/passport/login'

form_data ={
    'ck':'',
    'name':'18144024290',
    'password':'Jiuyue@11360',
    'remember':'false',
    'ticket':''
}
response =s.post(url1,data =form_data,headers =headers)

url2 = 'https://accounts.douban.com/passport/setting'
response2 =s.get(url2,headers =headers).text
print(response.text)

# with open('profile.html','w+') as f:
#     f.write(response2.text)
