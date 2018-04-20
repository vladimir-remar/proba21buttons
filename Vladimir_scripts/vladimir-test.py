#!/usr/bin/python
# -*- coding:utf-8 -*-
#autor: Vladimir Remar
#-----------------------------------------------------------------------

########################################################################
# Imports
########################################################################

import scrapy,os,sys,argparse
from urlparse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

########################################################################
# Arguments
########################################################################

parser = argparse.ArgumentParser(description='A basic Crawling  for specific webs') 
parser.add_argument('-l','--link', dest='link', help="Link d'una web", type=str,metavar="link-a-fer-crawling", required=True)

args=parser.parse_args()

WEB = [args.link]
DOMAINS = ['naturalbylila.com','goiclothing.com']

########################################################################
# Funcions
########################################################################

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
  
########################################################################
# Gestio Entrada
########################################################################

web1 = False

if urlparse(args.link).netloc not in DOMAINS:
  exit(1)
elif urlparse(args.link).netloc == DOMAINS[0]:
  web1 = True
#Fa falta un control, per dir que realment estem veiem un producte

########################################################################
# Creació resposta
########################################################################

class ProductosSpider(scrapy.Spider):
    name = "productos"
    allowed_domains = ["https://naturalbylila.com/", "https://goiclothing.com/"]
    
    def start_requests(self):
        global WEB
        
        for url in WEB:
            yield scrapy.Request(url=url, callback=self.parse)
    
    if web1:
    #Construcctor per la web naturalbylila.com
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
    else:
      #Construcctor per la web goiclothing.com
      def parse (self, response):
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




########################################################################
# Sortida
########################################################################

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'result.json'
})

process.crawl(ProductosSpider)
process.start() 

exit(0)
