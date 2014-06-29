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
        self.index_title = 'Gogistics'
        self.founder = 'Alan Tai'
        self.google_apps = 'Google Apps'
        self.google_apps_engine = 'Google Apps Engine'
    
#Chinese
class KeysValuesChinese():
    def __init__(self):
        self.index_title = u'資雲科技'
        self.founder = u'戴立舟'
        self.google_apps = u'Google應用程式集'
        self.google_apps_engine = u'資雲科技(Google Apps Engine)'