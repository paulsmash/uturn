from scrapy.contrib.spiders import CrawlSpider
from scrapy.item import Item, Field
from scrapy.conf import settings
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

import cStringIO as StringIO
import pprint
from scrapy.spider import Spider
from pyparsley import PyParsley
import config

from scrapy.contrib.loader import ItemLoader
from uturn.items import GalleryItem, GalleryItemLoader

class UturnItem(Item):
    def __init__(self, parslet_code, *args, **kwargs):
        for name in parslet_code.keys():
            self.fields[name] = Field()
            #print name
        super(UturnItem, self).__init__(*args, **kwargs)
 
YOUTUBE_PARSLET = {
     "title": "h1",
     "desc": ".description",
     "rating": ".ratingL @title",
     "embed": "#embed_code @value"
}

FAP_PARSELET = {
  "title": "title",
  "galls": [{
	  "title": "a.gal_title",
      "url": "a.gal_title @href",
	   "poster": ".avatar",
       "thumbs(img.gal_thumb)": [{
	           "src": "@src"
       }]
}]
}

class UturnSpider(CrawlSpider):
    name = "uturnspider"
    query = "cars"
    
    allowed_domains = ["imagefap.com"]
    start_urls = ['http://www.imagefap.com/gallery.php']

    rules = (
    #    Rule(SgmlLinkExtractor(allow=(r'results\?search_query=%s&page=\d+' %
     #                                 query,))),
        Rule(SgmlLinkExtractor(allow=(r'gallery\.php\?gid=',),
                              restrict_xpaths=['//div[@id="results-main-content"]']),
           'parse_gallery'),
    )
    
    def parse_gallery(self, response):
        exit(response)
    
    def __init__(self, parseletfile=None):
        if parseletfile:
            with open(parseletfile) as jsonfp:
                
                self.parselet = PyParsley(jsonfp)
        else:
            #print "using T1"
            self.parselet = PyParsley(FAP_PARSELET)
            
    def parse(self, response):
        
        if(self.parselet):
          parselet4 = PyParsley(FAP_PARSELET)
          
          extract = parselet4.parse(file = "http://www.imagefap.com/gallery.php", output = "python")
          #extract = parselet4.parse(string=config.gallery_php, output = "python")
          
          #l = GalleryItemLoader(item=GalleryItem, response=response)
          for g in extract["galls"]:
              #self.log("###%s" % g["title"])
              res = GalleryItem(g)
              #res["title"] = g["title"]
              yield res
        
    def parse_parsley(self, response):
      exit()
      parslet = PyParsley(T1, output='python') 
      res = UturnItem(T1, parslet.parse(string=response.body))
      pprint.pprint(res)
      print "parsley end"
      return res