
'''
数据采集，
http协议：

get\post 请求
请求和返回结构：http头、http主体、返回码（F12、Network、Headers）
    Status Code 返回码 200表示正确
    r.text可以提前网页内容

requests.get(url,params,headers,timeout)
url：目标 URL（必填）
params：字典或字符串，用于构造 URL 查询参数（
headers‌：自定义请求头（如模拟浏览器）
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
timeout‌：设置超时时间（秒），避免程序无限等待


'''


# get请求
import requests
import re
url = 'https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=%E7%A7%91%E6%AF%94'
data = {'key': 'value', 'abc': 'xyz'}
# get是使用get方式请求url,字典类型的data不用进行额处理
r = requests.get(url,data)
print(r.status_code)
content =r.text
print(content)
'''
response.status_code：HTTP 状态码（如 200 表示成功）
response.text：响应内容（字符串，自动解码）
response.content：响应内容（字节流，适合保存图片等二进制文件）
response.json()：将 JSON 响应解析为 Python 字典/列表
response.headers：服务器返回的响应头
response.encoding：检测到的编码格式（可手动设置，如 response.encoding = 'utf-8'）
'''


'''
用正则表达式匹配数据， r'',要匹配的内容，
    匹配固定的开头字符串+"(.*?xx)"括号里是要捕获的内容,.*?任意字符串
'''
# pattern = re.compile( r'"img":"(.*?\.jpg)"',re.S)
# results=re.findall(pattern,content)
# print(results)

# for result in results:
#     url,name=result
#     print(url,re.sub('\s','',name))


'''BeautifulSoup
格式化输出网页内容
'''

from bs4 import BeautifulSoup

# 示例HTML
# 创建BeautifulSoup对象
# soup = BeautifulSoup(content, 'html.parser')  # 使用Python内置解析器
# 或使用lxml解析器（推荐）
soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())  # 格式化输出



# 找到标题标签
print('*'*10)
print(f'找到标题标签:{soup.title}')

# ## title标签里的内容
# 打印（soup.title.string）
print('*'*10)
print(f'title标签里的内容:{soup.title.string}')

# 找到p标签
print('*'*10)
print(f'找到p标签:{soup.p}')

# ##找到p标签类的名字
# 打印（soup.p [ '类']）
# ##找到第一个a标签
print('*'*10)
print(f'找到第一个a标签:{soup.a}')
# ##找到所有的一个标签
# 打印（soup.find_all（ 'A'））
#
#
# ##找到id为imgs_json的的标签
# print(f'找到id为imgs_json的的标签:{soup.find(id = "imgs_json")}')
# 获取所有图片的src
images = soup.find_all('img')
num = 0
for img in images:
    src = img.get('src')
    alt = img.get('alt', '无替代文本')  #提供默认值
    print(f'图片地址: {src}, 替代文本: {alt}')
    # url = src
    # r =requests.get(url)
    # num += 1
    # with open(f'imgs/{url.split('/')[-1]}.jpg','wb') as f:
    #     f.write(r.content)
# #找到所有<a>标签的链接
# 在soup.find_all（ 'A'）链接：
#       打印（link.get（ 'HREF'））
# print('*'*10)
# print(soup.find_all('A'))
# ##找到文档中所有的文本内容
# print(soup.get_text())

# url ='http://www.cnu.cc/uploads/avatar/images/fd09cc61a86a5b07740a40f690f8027f_100.jpg'
# with open(f'E:/python_file/{url.split('/')[-1]}','wb') as f:
#     f.write(r.content)
