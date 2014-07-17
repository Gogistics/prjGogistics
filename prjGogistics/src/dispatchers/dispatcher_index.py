# -*- coding: utf-8 -*-
'''
Created on May 21, 2014

@author: Alan Tai

@Discription:
The project is for developing the company web-site. The part is the view controller of dispatching url paths
'''
import json

__author__ = 'Alan Tai<gogistics@gogistics-tw.com>'
import webapp2
import jinja2
import os
from dictionaries.dict_keys_values import KeysVaulesGeneral, KeysValuesMandarin,\
    KeysValuesEnglish
from dictionaries.dict_html_pages import HtmlPagesReference

#append templates' path directory
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('static/templates'))  # append templates' path
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

#dictionaries instances
keys_values_general = KeysVaulesGeneral()
keys_values_chinese = KeysValuesMandarin()
keys_values_english = KeysValuesEnglish()

#html reference
html_pages_ref = HtmlPagesReference()


#index handler
class IndexHandler(webapp2.RequestHandler):
    def get(self):
        title_chinese = keys_values_chinese.index_title
        template_values = {'token_html_page':keys_values_general.token_index_page}
        template_values.update({'title':title_chinese})
        template = jinja_environment.get_template(html_pages_ref.html_index)
        self.response.out.write(template.render(template_values))
        
class IndexLanguageVersionHandler(webapp2.RequestHandler):
    def post(self):
        assert self.request.get('fmt'), 'data format is not available'
        assert self.request.get('json_language_version_request'), 'request content is not available'
        
        json_obj = {}
        if self.request.get('fmt') == 'json':
            json_obj = json.loads(self.request.get('json_language_version_request'))
        
        token_html_page = json_obj['token_html_page']
        requested_language = json_obj['language']
        
        ajax_response = {'requst_status' : 'unknown'}
        if requested_language == 'mandarin' and token_html_page == keys_values_general.token_index_page:
            ajax_response['company_introduction_selector'] = u'公司簡介'
            ajax_response['cloud_services_introduction_selector'] = u'雲端服務簡介'
            ajax_response['contact_information_selector'] = u'連絡資訊'
            
            ajax_response['company_introduction_content'] = u'資雲科技'
            ajax_response['cloud_services_introduction_content'] = u'Google雲端服務整合'
            ajax_response['contact_information_content'] = u'連絡在雲端'
            ajax_response['language'] = 'mandarin'
            ajax_response['request_status'] = 'success'
        
        elif requested_language == 'english' and token_html_page == keys_values_general.token_index_page:
            ajax_response['company_introduction_selector'] = 'Company Introduction'
            ajax_response['cloud_services_introduction_selector'] = 'Cloud Service Introduction'
            ajax_response['contact_information_selector'] = 'Contact Information'
            
            ajax_response['company_introduction_content'] = 'Gogistics Introduction'
            ajax_response['cloud_services_introduction_content'] = 'Google Cloud Services Introduction'
            ajax_response['contact_information_content'] = u'Contact via Cloud'
            ajax_response['language'] = 'english'
            ajax_response['request_status'] = 'success'
        
        else:
            ajax_response['company_introduction_selector'] = u'公司簡介'
            ajax_response['cloud_services_introduction_selector'] = u'雲端服務簡介'
            ajax_response['contact_information_selector'] = u'連絡資訊'
            
            ajax_response['company_introduction_content'] = u'資雲科技'
            ajax_response['cloud_services_introduction_content'] = u'Google雲端服務整合'
            ajax_response['contact_information_content'] = u'連絡在雲端'
            
            ajax_response['request_status'] = 'success'
            
        self.response.out.headers['Content-Type'] = 'text/json'
        self.response.out.write(json.dumps(ajax_response))

#url dispatcher
app = webapp2.WSGIApplication([('/', IndexHandler),
                               ('/index_language_version_handler', IndexLanguageVersionHandler)], debug=True)