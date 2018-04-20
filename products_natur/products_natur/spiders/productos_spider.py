# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector

def gestio_colors(lista):
  '''
    Funcio per gestionar la sortida de colors
  '''
  colors = lista[1:]
  name   = '' 
  res    = []
  
  for color in colors:
    name = '{"name":"%s"}'%(color)
    if name not in res:
      res.append(name)
  
  return res
  
class QuotesSpider(scrapy.Spider):
    name = "productos_natur"
    
    def start_requests(self):
      
      start_urls = [
        'https://naturalbylila.com/producto/sudadera-usa/',
        'https://naturalbylila.com/producto/top-bimba/',
    ]
      for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        des           = response.css('div.post-content').extract_first()
        tag           = response.css('span.posted_in').extract_first()
        elemColrs     = response.css('select#color').extract_first()
        lElemColors   = Selector(text=elemColrs).xpath('//option/text()').extract()
        lColors       = gestio_colors(lElemColors)
        
        yield {
            'name' : response.css('h2.product_title.entry-title::text').extract_first(),
            'price': response.css('span.woocommerce-Price-amount.amount::text')[0].extract(),
            'image_urls': response.xpath('//a[contains(@href, "wp-content")]/img/@src').extract(),
            'title1' : Selector(text=tag).xpath('//a/text()').extract_first(),
            'colors': lColors,
            'description' : Selector(text=des).xpath('//p/text()').extract_first(),
            
        }
