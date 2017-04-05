# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse        #调用parse.urljoin()拼接baseURL与文章URL
from scrapy3.items import JobboleItem
from scrapy3.tools.common import url_to_md5

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        #获取所有文章 URL, 再调用detail_parse方法获取文章详情页
        #title = response.xpath('//a[@class="archive-title"/text()]').extract()
        #article_urls = response.xpath('//a[@class="archive-title"]//@href').extract()
        article_nodes = response.xpath('//div[@class="post-thumb"]/a')
        for article_node in article_nodes:
            article_url = article_node.xpath('@href').extract_first('')
            article_img = article_node.xpath('.//img/@src').extract_first('')
            yield Request(url=parse.urljoin(response.url,article_url),meta={'cover_img':article_img},callback=self.parse_detail)   #callback回调parse_detail

        #获取下一页URL, extract_first("")取第一个值
        next_page = response.xpath('//a[contains(@class,"next")]/@href').extract_first("")
        if next_page:
            yield Request(url=parse.urljoin(response.url,next_page),callback=self.parse)

    def parse_detail(self, response):
        #实例化JobboleItem
        jobbole_item = JobboleItem()

        #解析字段
        article_url = response.url
        cover = response.meta.get('cover_img','')   #封面图URL
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first('')
        time = response.xpath('//div[@class="entry-meta"]/p/text()').extract()[0].strip()[:10]
        content = ''.join([i.strip() for i in  response.xpath('//div[@class="entry"]//p//following-sibling::*[not(div)]/descendant-or-self::*/text()').extract()])
        tag = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract_first('')

        #将字段加入item
        jobbole_item['article_url'] = article_url
        jobbole_item['url_object_id'] = url_to_md5(article_url)
        jobbole_item['cover'] = [cover]             #该值应是可迭代类型，否则报错
        jobbole_item['title'] = title
        jobbole_item['time'] = time
        jobbole_item['content'] = content
        jobbole_item['tag'] = tag

        yield jobbole_item