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
        
        #
        self.company_introduction = u'Company Introdcution'
        self.cloud_service_introduction = u'Could Services Introduction'
        self.cloud_services_integration = u'Cloud Services Integration'
        self.contact_information = u'Contact Information'
        self.company_introduction_content = u'"Learn The Technology, Connect the World"'
        self.cloud_service_introduction_content = u'Introduction of cloud services'
        self.cloud_services_integration_content = u'Integrations of cloud services'
        self.contact_information_content = u'contact me via cloud'
        
        self.contact_message_name = 'Sender Name'
        self.contact_message_email = 'Sender Email'
        self.contact_message_subject = 'Subject'
        self.contact_message_body = 'Body'
        
        #
        self.btn_rewrite = u'Rewrite'
        self.btn_send = u'Send'
        
    
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
        self.cloud_service_introduction = u'雲端服務'
        self.cloud_services_integration = u'整合應用'
        self.contact_information = u'聯絡資訊'
        
        #
        self.company_introduction_content = u'"知識串起世界各角落"'
        self.cloud_service_introduction_content = u'雲端就是提供你服務的地方，當你有需要時可以在任何時間地點用來儲存資料、執行應用程式。跟需要下載的桌面應用程式不同，雲端服務可以透過網路和行動裝置在任何時間地點使用。'
        self.cloud_services_integration_content = u'雲端服務整合應用'
        self.contact_information_content = u'聯絡在雲端'
        
        #
        self.contact_message_name = u'寄件人姓名'
        self.contact_message_email = u'寄件者電子郵件'
        self.contact_message_subject = u'主旨'
        self.contact_message_body = u'內容'
        
        #
        self.btn_rewrite = u'重填'
        self.btn_send = u'寄送'
        
        