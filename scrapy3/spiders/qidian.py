#coding:utf8

import scrapy
from urllib import parse
from scrapy.http import Request

class XxsySpider(scrapy.Spider):
    name = 'qidian'                                     #项目名，全scrapy唯一
    #alowed_domains = ["qidian.com"]                   #Spider的爬行域，不在domain的URL将不爬行
    start_urls = ["http://a.qidian.com/"]               #Spider启动时进行爬行的URL列表

    def parse(self, response):
        #获取当前页面所有文章URL并传入parse_detail解析文章内容
        article_urls = response.xpath('//div[@class="book-mid-info"]/h4//a/@href').extract()
        for article_url in article_urls:
            yield Request(parse.urljoin(response.url,article_url), callback=self.parse_description)

        #获取下一页URL并调用parse重复执行爬行
        pageNum = response.xpath('//div[@id="page-container"]/@data-pagemax').extract_first()
        for page in range(2,int(pageNum)):
            yield Request('{}?page={}'.format(response.url,page),callback=self.parse)

    def parse_description(self, response):
        title = response.xpath('//div[contains(@class,"book-info")]//em/text()').extract_first()
        description = ''.join([ i.strip() for i in response.xpath('//div[@class="book-intro"]/p/text()').extract()])
        chapter = response.xpath('//ul[@class="cf"]//a/text()').extract()
        chapter_urls = response.xpath('//ul[@class="cf"]//a/@href').extract()
        for chapter_url in chapter_urls:
            yield Request(parse.urljoin(response.url, chapter_url), callback=self.parse_detail)

    def parse_detail(self, response):
        content = ''.join([i.strip() for i in response.xpath('//div[contains(@class,"read-content")]/p/text()').extract()])
        pass
