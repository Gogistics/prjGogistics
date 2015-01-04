# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler
from models.models_wine_info import WebLinkRoot, WebLinkWineTemp, WebLinkWine
from dictionaries.dict_key_value_pairs import KeyValuePairsGeneral
from bs4 import BeautifulSoup
import webapp2, logging, re, urllib2, urlparse


#
dict_general = KeyValuePairsGeneral()

class TaskCrawlerGeneralWineInfoDispatcher(BaseHandler):
    def get(self):
        self._read_feed()
    
    def _read_feed(self):
        """ crawling task """
        # temp root links
        list_webInfo_temp = [{"title" : "K&L", "link" : 'http://www.klwines.com/'}, {"title" : "BenchMarkWine", "link" : 'https://www.benchmarkwine.com/'}, {"title" : "WineBid", "link" : 'http://www.winebid.com/'}, {"title" : "BelmontWine", "link" : 'http://www.belmontwine.com/'}, {"title" : "The Wine Club", "link" : 'http://www.thewineclub.com/'}] # sample links
        
        # construct search list
        search_list = []
        query_root_entities = WebLinkRoot.query()
        if query_root_entities.count() != 0:
            root_list = []
            for entity in query_root_entities:
                root_list.append({"title" : entity["title"] , "link" : entity["link"]})
                
            if len(root_list) != 0:
                search_list.append(root_list)
            else:
                search_list.append(list_webInfo_temp)
            
        query_wine_entities = WebLinkWineTemp.query()
        if query_wine_entities.count() != 0:
            wine_links = [] # links are going to be searched
            for entity in query_wine_entities:
                wine_links.append({"title" : entity["title"] , "link" : entity["link"]})
                entity.key.delete()
                
            search_list.append(wine_links)
            
        
        # crawl
        count = 0 # count is used as a threshold to limit the app to consume quota
        while len(search_list) > 0 and count < 8:
            #
            sub_list = search_list.pop(0)
            for elem in sub_list:
                # root elem
                parsed = urlparse.urlsplit(elem["href"])
                link_base = "{url_scheme}://{url_netloc}/".format(url_scheme = parsed.scheme, url_netloc = parsed.netloc)
                
                req = urllib2.Request(elem["href"])
                response = urllib2.urlopen(req)
                searched_page = response.read()
                soup = BeautifulSoup(searched_page)
                
                new_sub_list = []
                for found_link in soup.find_all('a'):
                    if found_link.get('href'):
                        match_group = re.match("http", found_link.get('href'), re.I)
                        full_href = ""
                        
                        # not done yet
                        if not match_group:
                            full_href = "{href_link_base}{sub_href}".format(href_link_base = link_base, sub_href = found_link.get('href'))
                        else:
                            full_href = found_link.get('href')
                            
                        new_sub_list.append(full_href)
                        
                search_list.append(new_sub_list)
            
            count = count + 1
            
        # insert urls to WebLinkWineTemp
        while len(search_list) > 0:
            sub_list = search_list.pop()
            for elem in sub_list:
                new_link = WebLinkWineTemp()
                new_link.link = elem["link"]
                new_link.title = elem["title"]
                new_link.put()                

 
class TaskCategorizeWineInfoDispatcher(BaseHandler):
    def get(self):
        """ cron task """
        self._categorize()
        
    def _categorize(self):
        """ categorize wine info """
        entities = WebLinkWineTemp.query()
        for entity in entities:
            result = re.findall(r"BuyWine/Item|sku|skuIT|bwe|wines", entity["link"], re.I) # sku ; BuyWine/Item ; bwe
            query = WebLinkWine.query(WebLinkWine.link == entity["link"])
            if result and query.count() == 0:
                new_wine_info = WebLinkWine()
                new_wine_info.link = entity["link"]
                new_wine_info.title = entity["title"]
                new_wine_info.put()


# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/cron_tasks/crawler_wine_searcher', TaskCrawlerGeneralWineInfoDispatcher, name = 'crawler_wine_searcher'),
    webapp2.Route(r'/cron_tasks/categorize_wine_info', TaskCategorizeWineInfoDispatcher, name = "categorize_wine_info")
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG)