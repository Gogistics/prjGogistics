# -*- coding: utf-8 -*-
'''
Created on Dec 24, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler
from dictionaries.dict_key_value_pairs import KeyValuePairsGeneral
import jinja2, webapp2, logging, json, re, urllib2

# jinja environment
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))

# dict
dict_general = KeyValuePairsGeneral()

class QueryWineSearcherDispatcher(BaseHandler):
    def post(self):
        """ query mechanism for wine searcher """
        query_info = self.request.get('query_info')
        query_info = re.sub(r' ','+',query_info)
        query_vintage = self.request.get('query_vintage')
        
        # query_str = GLOBAL_VALUES.WINE_SEARCHER_API_KEY + "&Xformat=J" + "&Xwinename=" + "stag+leap+napa+usa" + "&Xvintage=" + "1999" + "&Xlocation=" + "&Xautoexpand=Y" + "&Xcurrencycode=usd" + "&Xkeyword_mode=X" + "&Xwidesearch=V";
        # average price of the wine
        query_str = dict_general.wine_searcher_api
        query_str += '&Xformat=J' + '&Xlocation=usa' + "&Xautoexpand=Y" + "&Xcurrencycode=usd" + "&Xkeyword_mode=X" + "&Xwidesearch=V"
        query_str += '&Xwinename=' + query_info
        query_str += '&Xvintage=' + query_vintage
        
        wine_searcher_query = urllib2.Request(query_str)
        wine_searcher_response = urllib2.urlopen(wine_searcher_query).read()
        
        # store selling the wine
        
        # vintage available at the query location
        
        
        ajax_response = {'processing_status' : wine_searcher_response}
        self.response.out.headers['Content-Type'] = 'text/json'
        self.response.out.write(json.dumps(ajax_response))

    
# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/query/wine_searcher', QueryWineSearcherDispatcher, name='wine_searcher')
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG)