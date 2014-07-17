'''
Created on Jul 17, 2014

@author: Alan Tai
'''
from dictionaries.dict_keys_values import KeysValuesMandarin, KeysVaulesGeneral

class MandarinHandler():
    def __init__(self):
        self.dict_keys_values_english = KeysVaulesGeneral()
        self.dict_keys_values_mandarin = KeysValuesMandarin()
    
    def handle_index_page_info(self):
        index_page_info = {}
        index_page_info.update({'brand_title':self.dict_keys_values_general.brand_title})
        index_page_info.update({'title':self.dict_keys_values_mandarin.index_page_title})
        return index_page_info
    
    def handle_admin_page_info(self):
        pass
    
    def handle_customer_services_page_info(self):
        customer_services_page_info = {}
        customer_services_page_info.update({'brand_title':self.dict_keys_values_general.brand_title})
        customer_services_page_info.update({'title':self.dict_keys_values_mandarin.customer_services_page_title})
        return customer_services_page_info