# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item, Field


class EasyodItem(scrapy.Item):
    description = Field()
    url = Field()
