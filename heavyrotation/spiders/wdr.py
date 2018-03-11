# -*- coding: utf-8 -*-
import scrapy
from libs.wdr import playlist

class WdrSpider(scrapy.Spider):
    name = 'wdr'
    allowed_domains = ['wdr.de']
    start_urls = ['http://wdr.de/']

    def parse(self, response):
        pl = playlist(response)
