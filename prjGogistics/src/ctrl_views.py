# -*- coding: utf-8 -*-
'''
Created on May 21, 2014

@author: Alan Tai

@Discription:
The project is for developing the company web-site. The part is the view controller of dispatching url paths
'''
import webapp2
import jinja2
import os

#append templates' path directory
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/static/templates'))  # append templates' path

#index handler
class GogisticsIndexHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template_values.update({'title':'Gogistics'})
        template = jinja_environment.get_template('/gogistics_index.html')
        self.response.out.write(template.render(template_values))

#url dispatcher
app = webapp2.WSGIApplication([('/', GogisticsIndexHandler)], debug=True)