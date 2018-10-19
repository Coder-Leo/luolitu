# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class SwmtSpider(Spider):
    name = 'swmt'
    allowed_domains = ['luolitu.com']
    start_urls = ['http://www.luolitu.com/catalog/siwameitui.html']

    '''
    def start_requests(self):
        base_url = 'http://www.luolitu.com/catalog/siwameitui'
        for page in range(1, self.settings.get('MAX_PAGE_SWMT') + 1):
            if page == 1:
                url = base_url + '.html'
            else:
                url = base_url + '_{}.html'.format(page)
            yield Request(url, self.parse)
    '''

    def parse(self, response):
        base_url = 'http://www.luolitu.com/catalog/siwameitui'
        # 找到总页数
        total_page = response.xpath('//div[@id="content"]/ul[@class="pager"]//li[last() - 1 ]/a/text()').extract_first()
        # print('@@total page: ', total_page)

        # 生成全部页面的请求
        for page in range(1, int(total_page) + 1):
            if page == 1:
                url = base_url + '.html'
            else:
                url = base_url + '_{}.html'.format(page)
            yield Request(url, self.parse)

        pics_url = response.xpath('//ul[@id="lazyed"]//li/a/@href').extract()
        print('# pic url:', pics_url)

        # 获取每个模特的所有图链接
        for url in pics_url:
            yield response.follow(url, self.parse_single_girl)

    def parse_single_girl(self, response):
        print('------')
        title = response.xpath('//div[@id="heading"]/h1/text()').extract_first()
        imgs_url = response.xpath('//div[@class="noshow"]//img/@data-img').extract()
        print(title, ': ', imgs_url)