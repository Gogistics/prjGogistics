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
from dict_keys_values import Keys_Values_Chinese

#append templates' path directory
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))  # append templates' path

#index handler
class GogisticsIndexHandler(webapp2.RequestHandler):
    def get(self):
        title_english = Keys_Values_Chinese().index_title
        template_values = {}
        template_values.update({'title':title_english})
        template = jinja_environment.get_template('/gogistics_index.html')
        self.response.out.write(template.render(template_values))

#url dispatcher
app = webapp2.WSGIApplication([('/', GogisticsIndexHandler)], debug=True)