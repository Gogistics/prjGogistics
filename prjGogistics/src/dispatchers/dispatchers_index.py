# -*- coding: utf-8 -*-
'''
Created on May 21, 2014

@author: Alan Tai

@Discription:
The project is for developing the company web-site. The part is the view controller of dispatching url paths
'''
__author__ = 'Alan Tai<gogistics@gogistics-tw.com>'


import json
import logging
from handlers_general.handler_languages_versions import MandarinHandler,\
    EnglishHandler
import webapp2
import jinja2
import os
from dictionaries.dict_keys_values import KeysVaulesGeneral, KeysValuesMandarin,\
    KeysValuesEnglish
from dictionaries.dict_html_pages import HtmlPagesReference
from google.appengine.api import taskqueue

#append templates' path directory
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))  # append templates' path
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

#dictionaries instances
keys_values_general = KeysVaulesGeneral()
keys_values_mandarin = KeysValuesMandarin()
keys_values_english = KeysValuesEnglish()

#html reference
html_pages_ref = HtmlPagesReference()
language_handler_madarin = MandarinHandler()
language_handler_english = EnglishHandler()


#index handler
class IndexPageDispatcher(webapp2.RequestHandler):
    def get(self):
        ''' index dispatcher '''
        
        # for gcm demo use; for testing only
        # taskqueue.add(url = '/gcm_send_message')
        
        # index context
        template_values = {}
        template_values.update(language_handler_madarin.handle_index_page_info())
        template = jinja_environment.get_template(html_pages_ref.html_index)
        self.response.out.write(template.render(template_values))
        
class IndexContactMessageDispatcher(webapp2.RequestHandler):
    def post(self):
        pass
        
class IndexLanguageVersionDispatcher(webapp2.RequestHandler):
    def post(self):
        assert self.request.get('fmt'), 'data format is not available'
        assert self.request.get('json_language_version_request'), 'request content is not available'
        
        json_obj = {}
        if self.request.get('fmt') == 'json':
            json_obj = json.loads(self.request.get('json_language_version_request'))
        
        token_html_page = json_obj['token_html_page']
        requested_language = json_obj['language']
        
        ajax_response = {}
        if requested_language == 'mandarin' and token_html_page == keys_values_general.token_index_page:
            ajax_response.update(language_handler_madarin.handle_index_page_info())
            ajax_response['request_status'] = 'success'
        
        elif requested_language == 'english' and token_html_page == keys_values_general.token_index_page:
            ajax_response.update(language_handler_english.handle_index_page_info())
            ajax_response['request_status'] = 'success'
        
        else:
            ajax_response.update(language_handler_madarin.handle_index_page_info())
            ajax_response['request_status'] = 'success'
            
        self.response.out.headers['Content-Type'] = 'text/json'
        self.response.out.write(json.dumps(ajax_response))

#url dispatcher
app = webapp2.WSGIApplication([('/', IndexPageDispatcher),
                               ('/index_language_version_handler', IndexLanguageVersionDispatcher)], debug=True)

#log 
logging.getLogger().setLevel(logging.DEBUG)
