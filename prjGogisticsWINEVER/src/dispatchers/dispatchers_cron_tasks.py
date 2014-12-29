# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler
from models.models_wine_info import WebLink
from dictionaries.dict_key_value_pairs import KeyValuePairsGeneral
from bs4 import BeautifulSoup
import webapp2, logging, re, urllib2


#
dict_general = KeyValuePairsGeneral()

class CrawlerGeneralWineInfoDispatcher(BaseHandler):
    def get(self):
        self._read_feed()
    
    def _read_feed(self):
        list_wine_weblinks = ['http://www.klwines.com/', 'http://www.winebid.com/'] # sample links
        
        for root_link in list_wine_weblinks:
            req = urllib2.Request(root_link)
            response = urllib2.urlopen(req)
            the_page = response.read()
            soup = BeautifulSoup(the_page)
            
            for link in soup.find_all('a'):
                if link.get('title') and link.get('href'):
                    m = re.match("http", link.get('href'), re.I)
                    full_href = ""
                    if not m:
                        full_href = "{href_root_link}{sub_href}".format(href_root_link = root_link, sub_href = link.get('href'))
                    else:
                        full_href = link.get('href')
                        
                    query_result = WebLink.query(WebLink.link == full_href)
                    if (query_result.count() == 0):
                        new_link = WebLink()
                        new_link.link = full_href
                        new_link.title = link.get('title')
                        new_link.put()
                

# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/cron_tasks/crawler_wine_searcher', CrawlerGeneralWineInfoDispatcher, name='crawler_wine_searcher')
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG)