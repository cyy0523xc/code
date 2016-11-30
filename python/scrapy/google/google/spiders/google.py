# -*- coding: utf-8 -*-

#
# Author:
# Created Time: 2016年11月30日 星期三 14时52分12秒

import scrapy


class GoogleSpider(scrapy.Spider):
    name = "google"
    handle_httpstatus_list = [301, 302]

    def start_requests(self):
        urls = [
            'https://www.google.com.hk/search?q=%E9%A6%99%E6%B8%AF&newwindow=1&ie=UTF-8&tbm=nws&ei=Afo7WNGeGIzs0ATFtZKgBg&start=20&sa=N',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status in [301, 302]:
            url = response.xpath("/a/@href").extract()
            yield scrapy.Request(url=url[0], callback=self.parse)

        r = response.xpath("//div").extract()
        print("Length of div: %d" % len(r))

        r = response.xpath("//div[@class='g']").extract()
        print("Length of div g: %d" % len(r))
