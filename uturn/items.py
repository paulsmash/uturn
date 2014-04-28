# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join

	
class GalleryItem(Item):
    # define the fields for your item here like:
    # name = Field()
	title = Field()
	poster = Field()
	url = Field()
	thumbs = Field()
	
class GalleryItemLoader(ItemLoader):

    default_output_processor = TakeFirst()

    title_in = MapCompose(unicode.title)
    title_out = Join()

    poster = MapCompose(unicode.title)
    #title_out = Join()
    
    url_in = MapCompose(unicode.title)
    #url_out = Join()
    #thumbs_in = MapCompose(unicode.strip)
    # ...
 