# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ProductosSpider(scrapy.Spider):
    name = "productos_goi"
    
    def start_requests(self):
      start_urls = [
        'https://goiclothing.com/collections/ver-todo/products/pre-order-vestido-candince',
        'https://goiclothing.com/collections/ver-todo/products/pantalon-winona',
    ]
      for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
      elem_price  = response.css('span.money::text').extract_first()
      price       = elem_price [1:]
      elemDes     = response.css('div.product-single__description.rte').extract_first()
      des        = '\n'.join(Selector(text=elemDes).xpath('//p/text()').extract())
      yield {
          'name': response.css('h1.product-single__title::text').extract_first(),
          'price': price,
          'image_urls': response.xpath('//a[contains(@href, "products")]/img/@src').extract(),
          'description': des
      }
