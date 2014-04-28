# Scrapy settings for uturn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'uturn'

SPIDER_MODULES = ['uturn.spiders']
NEWSPIDER_MODULE = 'uturn.spiders'

ITEM_PIPELINES = {
  'uturn.pipelines.UturnPipeline' :10,
  'uturn.scrapymongodb.MongoDBPipeline' :90,
  }

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'items3'
#MONGODB_UNIQ_KEY = 'title'
MONGODB_ITEM_ID_FIELD = '_id'
MONGODB_SAFE = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'uturn (+http://www.yourdomain.com)'
