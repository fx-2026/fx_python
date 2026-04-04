import scrapy
from bs4 import BeautifulSoup
from stre_douban.items import StreDoubanItem

#修改输出的字符
import sys
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding ='gb18030')

class StreDoubanSpSpider(scrapy.Spider):
    name = "stre_douban_sp"#爬虫运行scrapy crawl stre_douban_sp --nolog(不打印调试的东西)
    allowed_domains = ["book.douban.com"]#允许的域名，限制广度，深度在setting里面
    start_urls = ["https://book.douban.com/top250"] #初始域名

#     j = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(11))#地址

# from time import sleep
# for url in j:
#     print(getdaoban(url))
#     sleep(30)
    #爬虫启动时，引擎自动调用该方法，并且只会调用一次，生成初始的请求对象
    #start_requests(),调用Request后生成对象返回到队列里引擎的队列里
    #引擎再向网站申请，下载页面
    def start_requests(self):
        for i in range (11):
            url=f'https://book.douban.com/top250?start={i * 25}'
            yield scrapy.Request(url = url,callback =self.parse)
            #yield相等于return
            #callback是回调函数，引擎会将下载好的页面（Response对象）回调给该方法
            #默认回调参数是parse

    def parse(self, response):
        new_response = BeautifulSoup(response.text, 'html.parser')
        result = BeautifulSoup.find_all.new_respon('div',attrs={'class':"pl2"})
        # print(result)
        for i in range(len(result)):
            item = StreDoubanItem()
            title = result[i].find('a').get('title')
            link = result[i].find('a').get('href')
            item['title'] = title
            item['link'] = link

            yield scrapy.Request(url = link,meta={'item': item} ,callback =self.parse2)
        
    def parse2(self, response):
        item = response.meta['item']
        new2_response = BeautifulSoup(response.text, 'html.parser')
        result = BeautifulSoup.find_all.new2_response('div',attrs={'class':"intro"}).get_text().strip()
        item['content'] = result
        yield item
