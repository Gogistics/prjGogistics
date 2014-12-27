# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler
from libs_crawler import feedparser
from models.models_wine_info import WebLink
from dictionaries.dict_key_value_pairs import KeyValuePairsGeneral

import webapp2, logging


#
dict_general = KeyValuePairsGeneral()

class CrawlerGeneralWineInfoDispatcher(BaseHandler):
    def get(self):
        self._read_feed()
    
    def _read_feed(self):
        feeds = feedparser.parse("http://www.wine-searcher.com/")
        
        for feed in feeds["items"]:
            queried_entities = WebLink.query(WebLink.link == feed["link"])
            if(queried_entities.count() == 0):
                new_link = WebLink()
                new_link.link = feed["link"]
                new_link.title = feed["title"]
                new_link.logo = feed["logo"]
                new_link.put()
                

# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/cron_tasks/crawler_wine_searcher', CrawlerGeneralWineInfoDispatcher, name='crawler_wine_searcher')
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG)