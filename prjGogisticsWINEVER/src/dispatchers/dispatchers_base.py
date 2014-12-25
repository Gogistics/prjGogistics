# -*- coding: utf-8 -*-
'''
Created on Dec 24, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler
from dictionaries.dict_key_value_pairs import KeyValuePairsGeneral
import jinja2, webapp2, logging

# jinja environment
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))

# dict
dict_general = KeyValuePairsGeneral()

class FrontPageDispatcher(BaseHandler):
    def get(self):
        template_values = {}
        template_values.update({'title' : 'WINEver'})
        self.render_template("/front_page_container.html", template_values)
    
# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/', FrontPageDispatcher, name='front_page')
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG)