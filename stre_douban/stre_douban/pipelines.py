# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StreDoubanPipeline:
    def __init__(self):
        self.article=open('./douban_book_scrapy.txt','a+',encoding='utf-8')
    
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        content =item['content']
        output = f'{title}\t{link}\t{content}\n\n'
        self.article.write(output)
        self.article.close()
        return item
    # def process_item(self, item, spider):
    #     return item
