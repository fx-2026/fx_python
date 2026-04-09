import scrapy
from bs4 import BeautifulSoup
from stre_douban.items import StreDoubanItem

#修改输出的字符
# import sys
# import io 
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding ='gb18030')

class StreDoubanSpSpider(scrapy.Spider):
    name = "stre_douban_sp"#爬虫运行scrapy crawl stre_douban_sp --nolog(不打印调试的东西)
    allowed_domains = ["book.douban.com"]#允许的域名，限制广度，深度在setting里面
    start_urls = ["https://book.douban.com/top250"] #初始域名

    #爬虫启动时，引擎自动调用该方法，并且只会调用一次，生成初始的请求对象
    #start_requests(),调用Request后生成对象返回到队列里引擎的队列里
    #引擎再向网站申请，下载页面
    # def start_requests(self):
    #     url='https://book.douban.com/top250?start=25'
        # headers = {
        #     # 伪装成最新版 Chrome 浏览器
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        #     # 关键：伪造来源，告诉服务器我是从豆瓣首页点进来的
        #     'Referer': 'https://book.douban.com/',
        #     # 告诉服务器我能处理压缩数据
        #     'Accept-Encoding': 'gzip, deflate',
        #     # 告诉服务器我接受多种格式
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     # 语言偏好
        #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # }
        # yield scrapy.Request(url = url,callback = self.parse)

    def start_requests(self):
        for i in range (11):
            url=f'https://book.douban.com/top250?start={i * 25}'
            yield scrapy.Request(url = url,callback =self.parse)
            # yield相等于return
            # callback是回调函数，引擎会将下载好的页面（Response对象）回调给该方法
            # 默认回调参数是parse

    def parse(self, response):
        # new_response = BeautifulSoup(response.text, 'html.parser')
        # result = BeautifulSoup.find_all.new_response('div',attrs={'class':"pl2"})
        book_items = response.css('div.pl2')

        # 遍历每一条书籍数据
        for book in book_items:
            item = StreDoubanItem()
            title = book.css('a::text').get().strip() # 提取书名
            link = book.css('a::attr(href)').get().strip() # 提取链接
        # 在这里打印或 yield item
            print(f"书名: {title}, 链接: {link}")
            item['title'] = title
            item['link'] = link
            # yield item
            yield scrapy.Request(url = link,meta={'item': item} ,callback =self.parse2)
        
    def parse2(self, response):
        item = response.meta['item']
        new_response =  response.css('div.intro')
        result = new_response.css('p ::text').get()
        print(result)
        item['content'] = result
        yield item
