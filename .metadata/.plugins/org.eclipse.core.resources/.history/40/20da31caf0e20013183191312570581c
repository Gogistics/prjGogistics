# -*- coding: utf-8 -*-
'''
Created on May 21, 2014

@author: Alan Tai
'''
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/static/templates'))  # append templates' path

class GogisticsIndexHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template_values.update({'title':'Gogistics Home'})
        template = jinja_environment.get_template('/gogistics_index.html')
        self.response.out.write(template.render(template_values))

# set url
app = webapp2.WSGIApplication([('/gogistics_index', GogisticsIndexHandler)], debug=True)