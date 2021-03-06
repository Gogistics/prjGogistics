'''
Created on Jul 17, 2014

@author: Alan Tai
'''
from dictionaries.dict_keys_values import KeysValuesMandarin, KeysVaulesGeneral, KeysValuesEnglish

class MandarinHandler():
    def __init__(self):
        self.dict_keys_values_general = KeysVaulesGeneral()
        self.dict_keys_values_mandarin = KeysValuesMandarin()
    
    def handle_index_page_info(self):
        index_page_info = {}
        index_page_info.update({'token_html_page':self.dict_keys_values_general.token_index_page})
        index_page_info.update({'title':self.dict_keys_values_mandarin.index_page_title})
        
        #selector
        index_page_info.update({'company_introduction_selector' : self.dict_keys_values_mandarin.company_introduction})
        index_page_info.update({'cloud_services_introduction_selector' : self.dict_keys_values_mandarin.cloud_service_introduction})
        index_page_info.update({'cloud_services_integration_selector' : self.dict_keys_values_mandarin.cloud_services_integration})
        index_page_info.update({'contact_information_selector' : self.dict_keys_values_mandarin.contact_information})
        
        #content
        index_page_info.update({'company_introduction_content' : self.dict_keys_values_mandarin.company_introduction_content})
        index_page_info.update({'cloud_services_introduction_content': self.dict_keys_values_mandarin.cloud_service_introduction_content})
        index_page_info.update({'cloud_services_integration_content' : self.dict_keys_values_mandarin.cloud_services_integration_content})
        index_page_info.update({'contact_information_content' : self.dict_keys_values_mandarin.contact_information_content})
        
        index_page_info.update({'contact_message_name':self.dict_keys_values_mandarin.contact_message_name})
        index_page_info.update({'contact_message_email':self.dict_keys_values_mandarin.contact_message_email})
        index_page_info.update({'contact_message_subject':self.dict_keys_values_mandarin.contact_message_subject})
        index_page_info.update({'contact_message_body':self.dict_keys_values_mandarin.contact_message_body})
        
        index_page_info.update({'btn_rewrite':self.dict_keys_values_mandarin.btn_rewrite})
        index_page_info.update({'btn_send':self.dict_keys_values_mandarin.btn_send})
        
        index_page_info.update({'language' : 'mandarin'})
        
        return index_page_info
    
    def handle_customer_services_page_info(self):
        customer_services_page_info = {}
        customer_services_page_info.update({'title':self.dict_keys_values_mandarin.customer_services_page_title})
        return customer_services_page_info
    
    
class EnglishHandler():
    def __init__(self):
        self.dict_keys_values_general = KeysVaulesGeneral()
        self.dict_keys_values_english = KeysValuesEnglish()
    
    def handle_index_page_info(self):
        index_page_info = {}
        index_page_info.update({'token_html_page':self.dict_keys_values_general.token_index_page})
        index_page_info.update({'title':self.dict_keys_values_english.index_page_title})
        
        #
        index_page_info.update({'company_introduction_selector' : self.dict_keys_values_english.company_introduction})
        index_page_info.update({'cloud_services_introduction_selector' : self.dict_keys_values_english.cloud_service_introduction})
        index_page_info.update({'cloud_services_integration_selector' : self.dict_keys_values_english.cloud_services_integration})
        index_page_info.update({'contact_information_selector' : self.dict_keys_values_english.contact_information})
        
        #
        index_page_info.update({'company_introduction_content' : self.dict_keys_values_english.company_introduction_content})
        index_page_info.update({'cloud_services_introduction_content': self.dict_keys_values_english.cloud_service_introduction_content})
        index_page_info.update({'cloud_services_integration_content' : self.dict_keys_values_english.cloud_services_integration_content})
        index_page_info.update({'contact_information_content' : self.dict_keys_values_english.contact_information_content})
        
        index_page_info.update({'contact_message_name':self.dict_keys_values_english.contact_message_name})
        index_page_info.update({'contact_message_email':self.dict_keys_values_english.contact_message_email})
        index_page_info.update({'contact_message_subject':self.dict_keys_values_english.contact_message_subject})
        index_page_info.update({'contact_message_body':self.dict_keys_values_english.contact_message_body})
        
        index_page_info.update({'btn_rewrite':self.dict_keys_values_english.btn_rewrite})
        index_page_info.update({'btn_send':self.dict_keys_values_english.btn_send})
        
        
        index_page_info.update({'language' : 'english'})
        
        return index_page_info
    
    def handle_customer_services_page_info(self):
        customer_services_page_info = {}
        customer_services_page_info.update({'brand_title':self.dict_keys_values_general.brand_title})
        customer_services_page_info.update({'title':self.dict_keys_values_english.customer_services_page_title})
        return customer_services_page_info