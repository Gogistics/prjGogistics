# -*- coding: utf-8 -*-
'''
Created on Jun 24, 2014

@author: Alan Tai
'''
__author__ = 'Alan Tai'


from handlers.handler_webapp2_extra_auth import BaseHandler
import logging
import jinja2
import webapp2

# dictionaries

from dictionaries.dict_keys_values import KeysVaulesGeneral
dict_general = KeysVaulesGeneral()

# jinja environment
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))

# dispatchers
class FrontPageDispatcher(BaseHandler):
    def get(self):
        """ front page dispatcher """
        template_values = {}
        template_values.update({'title': dict_general.web_title_front_page})
        self.render_template(dict_general.front_page, template_values)
        
# dispatchers
class IndexPageDispatcher(BaseHandler):
    def get(self):
        """ front page dispatcher """
        template_values = {}
        template_values.update({'title':dict_general.web_title_index_page})
        self.render_template(dict_general.index_page, template_values)
        
class RegxTestDispatcher(BaseHandler):
    def get(self, regx_id):
        """ Regx testing path dispatcher """
        template_values = {}
        template_values.update({'title':u'Regx Demo' + regx_id })
        self.render_template(dict_general.index, template_values)

# configuration
config = dict_general.config_setting

# app
app = webapp2.WSGIApplication([
    webapp2.Route(r'/', FrontPageDispatcher, name='front_page'),
    webapp2.Route(r'/base/index', IndexPageDispatcher, name='index_page'),
    webapp2.Route(r'/base/test/<regx_id:\d+>', RegxTestDispatcher, name='regx_page')
], debug=True, config=config)

# log
logging.getLogger().setLevel(logging.DEBUG) 
    
