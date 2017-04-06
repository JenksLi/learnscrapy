# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter   #scrapy自带item导出为json方法

class Scrapy3Pipeline(object):
    def process_item(self, item, spider):
        return item

#自定义json导出
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = open('article.json','w',encoding='utf8')
    def process_item(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

#调用scrapy提供的json export导出json文件
class JsonExporterPipeline(object):
    def __init__(self):
        self.file = open('ArticleJosnExporter.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding='utf8',ensure_ascii=False)
        self.exporter.start_exporting()
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class ScrapyImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for status,value in results:
            cover_path = value.get('path','')
        item['cover_path'] = cover_path
        return item     #返回item