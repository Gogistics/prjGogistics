# -*- coding: utf-8 -*-
'''
Created on May 21, 2014

@author: Alan Tai

@Discription:
The project is for developing the company web-site. The part is the view controller of dispatching url paths
'''

__author__ = 'Alan Tai<gogistics@gogistics-tw.com>'
import webapp2
import jinja2
import os
from dictionaries.dict_keys_values import KeysVaulesGeneral, KeysValuesChinese,\
    KeysValuesEnglish
from dictionaries.dict_html_pages import HtmlPagesReference

#append templates' path directory
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))  # append templates' path
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

#dictionaries instances
keys_values_general = KeysVaulesGeneral()
keys_values_chinese = KeysValuesChinese()
keys_values_english = KeysValuesEnglish()

#html reference
html_pages_ref = HtmlPagesReference()


#index handler
class IndexHandler(webapp2.RequestHandler):
    def get(self):
        title_chinese = keys_values_chinese.index_title
        template_values = {'token':keys_values_general.token_index_page}
        template_values.update({'title':title_chinese})
        template = jinja_environment.get_template(html_pages_ref.html_index)
        self.response.out.write(template.render(template_values))

#url dispatcher
app = webapp2.WSGIApplication([('/', IndexHandler)], debug=True)