# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector


from easyod.items import EasyodItem


class JAODSpider(Spider):
    name = "easyod_main_spider"
    allowed_domains = ["juntadeandalucia.es"]
    start_urls = [
        "http://www.juntadeandalucia.es/datosabiertos/portal.html"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//a')
        items = []

        for site in sites:
            item = EasyodItem()
            item['description'] = site.xpath('text()').extract()
            item['url'] = site.xpath('@href').extract()
            items.append(item)

        return items