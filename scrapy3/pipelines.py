# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy.pipelines.images import ImagesPipeline

class Scrapy3Pipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json','a',encoding='utf8')
    def writeJson(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

class ScrapyImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for status,value in results:
            cover_path = value.get('path','')
        item['cover_path'] = cover_path
        return item     #返回item