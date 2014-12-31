# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler
from models.models_wine_info import WebLink, WebLinkRoot, WebLinkWineTemp
from dictionaries.dict_key_value_pairs import KeyValuePairsGeneral
from bs4 import BeautifulSoup
import webapp2, logging, re, urllib2, urlparse


#
dict_general = KeyValuePairsGeneral()

class CrawlerGeneralWineInfoDispatcher(BaseHandler):
    def get(self):
        self._read_feed()
    
    def _read_feed(self):
        """ crawling task """
        # temp root links
        list_webInfo_temp = [{"title" : "K&L", "elem" : 'http://www.klwines.com/'}, {"title" : "WineBid", "elem" : 'http://www.winebid.com/'}, {"title" : "BelmontWine", "elem" : 'http://www.belmontwine.com/'}] # sample links
        
        # construct search list
        search_list = []
        query_root_entities = WebLinkRoot.query()
        if query_root_entities.count() != 0:
            root_list = []
            for entity in query_root_entities:
                root_list.append({"title" : entity["title"] , "elem" : entity["elem"]})
                
            if len(root_list) != 0:
                search_list.append(root_list)
            else:
                search_list.append(list_webInfo_temp)
            
        query_wine_entities = WebLinkWineTemp.query()
        if query_wine_entities.count() != 0:
            wine_links = [] # links are going to be searched
            for entity in query_wine_entities:
                wine_links.append({"title" : entity["title"] , "elem" : entity["elem"]})
                entity.key.delete()
                
            search_list.append(wine_links)
            
        
        # crawl
        count = 0
        while len(search_list) > 0 or count < 8:
            sub_list = search_list.pop(0)
            
            for elem in sub_list:
                # root elem
                parsed = urlparse.urlsplit(elem["href"])
                link_base = "{0}://{1}/".format(parsed.scheme, parsed.netloc)
                
                req = urllib2.Request(elem["href"])
                response = urllib2.urlopen(req)
                searched_page = response.read()
                soup = BeautifulSoup(searched_page)
                
                new_sub_list = []
                for found_link in soup.find_all('a'):
                    if found_link.get('title') and found_link.get('href'):
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
            for sub_list in search_list:
                for elem in sub_list:
                    new_link = WebLinkWineTemp()
                    new_link.link = elem["link"]
                    new_link.title = elem["title"]
                    new_link.put()                
        # end

#         for root_link in list_webInfo_temp:
#             req = urllib2.Request(root_link)
#             response = urllib2.urlopen(req)
#             the_page = response.read()
#             soup = BeautifulSoup(the_page)
#             
#             for elem in soup.find_all('a'):
#                 if elem.get('title') and elem.get('href'):
#                     m = re.match("http", elem.get('href'), re.I)
#                     full_href = ""
#                     if not m:
#                         full_href = "{href_root_link}{sub_href}".format(href_root_link = root_link, sub_href = elem.get('href'))
#                     else:
#                         full_href = elem.get('href')
#                         
#                     query_result = WebLink.query(WebLink.link == full_href)
#                     if (query_result.count() == 0):
#                         new_link = WebLink()
#                         new_link.link = full_href
#                         new_link.title = elem.get('title')
#                         new_link.put()

# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/cron_tasks/crawler_wine_searcher', CrawlerGeneralWineInfoDispatcher, name='crawler_wine_searcher')
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG)