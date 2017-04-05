# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobboleItem(scrapy.Item):
    article_url = scrapy.Field()
    url_object_id = scrapy.Field()  #URL转换
    cover = scrapy.Field()          #文章封面图
    cover_path = scrapy.Field()     #封面图存放路径
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()