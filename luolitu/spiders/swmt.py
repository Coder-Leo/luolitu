# -*- coding: utf-8 -*-
import scrapy


class SwmtSpider(scrapy.Spider):
    name = 'swmt'
    allowed_domains = ['luolitu.com']
    start_urls = ['http://luolitu.com/']

    def parse(self, response):
        pass
