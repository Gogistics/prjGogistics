# -*- coding: utf-8 -*-
'''
Created on Dec 24, 2014

@author: Alan Tai
'''
from handlers.handler_webapp2_extra_auth import BaseHandler

import jinja2
# jinja environment
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))

class IndexDispatcher(BaseHandler):
    def get(self):
        template_values = {}
        template_values.update({})
        self.render_template("/index.html", template_values)
    