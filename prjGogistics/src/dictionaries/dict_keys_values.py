# -*- coding: utf-8 -*-
'''
Created on May 22, 2014

@author: Alan Tai

@description:
dictionary for key-value pairs
'''

class KeysVaulesGeneral():
    def __init__(self):
        self.website = 'http://gogistics.gotistics-tw.com'
        self.host_email = 'gogistics@gogistics-tw.com'
        self.mobile_tw = '+886-973-948-158'
        self.mobile_usa_ca = '+1-408-565-5133'
        
        #tokens
        self.token_index_page = 'index_page'
        self.token_questions_answer_page = 'questions_answer_page'
        self.token_client_services_page = 'client_services_page'
        
        
#Multi-languages dictionary
#English
class KeysValuesEnglish():
    def __init__(self):
        ''' init website information in english '''
        #
        self.index_page_title = 'Gogistics'
        self.founder = 'Alan Tai'
        self.google_apps = 'Google Apps'
        self.google_apps_engine = 'Google Apps Engine'
        
        
        self.company_introduction = u'Company Introdcution'
        self.cloud_service_introduction = u'Could Services Introduction'
        self.contact_information = u'Contact Information'
        self.company_introduction_content = u'Gogistics = Google + Logistics'
        self.cloud_service_introduction_content = u'Integration of google cloud services'
        self.contact_information_content = u'contact me via cloud'
    
#Chinese
class KeysValuesMandarin():
    def __init__(self):
        '''init website information in mandarin '''
        #
        self.index_page_title = u'資雲科技'
        self.founder = u'戴立舟'
        self.google_apps = u'Google應用程式集'
        self.google_apps_engine = u'資雲科技(Google Apps Engine)'
        
        #
        self.company_introduction = u'公司簡介'
        self.cloud_service_introduction = u'雲端服務簡介'
        self.contact_information = u'聯絡資訊'
        self.company_introduction_content = u'資雲科技'
        self.cloud_service_introduction_content = u'Google雲端服務整合'
        self.contact_information_content = u'聯絡在雲端'
        
        
        
        
        
        
        