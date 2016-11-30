# -*- coding: utf-8 -*-

#
# Author:
# Created Time: 2016年11月30日 星期三 14时52分12秒

import scrapy


class GoogleSpider(scrapy.Spider):
    name = "google"

    def start_requests(self):
        urls = [
            'https://www.google.com.hk/search?q=%E9%A6%99%E6%B8%AF&newwindow=1&ie=UTF-8&tbm=nws&ei=Afo7WNGeGIzs0ATFtZKgBg&start=20&sa=N',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
