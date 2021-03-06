'''
Created on Jul 23, 2014

@author: Alan Tai
'''
import webapp2
from models.models_gcm import GCMClientRegID
import json
import logging
from google.appengine.api import urlfetch

class GCMReceiveRegIDHandler(webapp2.RequestHandler):
    ''' handle received id '''
    def post(self):
        reg_id = self.request.get('registrationId')
        user_name = self.request.get('userName')
        
        ajax_response = {}
        queries_entity = GCMClientRegID().query(GCMClientRegID.reg_id == reg_id).get()
        if queries_entity:
            ajax_response['status'] = 'device id is already registered'
        else:
            new_reg_id = GCMClientRegID()
            new_reg_id.reg_id = reg_id
            new_reg_id.user_name = user_name
            new_reg_id.put()
            ajax_response['reg_id'] = reg_id
            
        self.response.out.headers['Content-Type'] = 'text/json'
        self.response.out.write(json.dumps(ajax_response))
    
class GCMSendHandler(webapp2.RequestHandler):
    ''' setup GCM send method '''
    def post(self):
        API_KEY = 'AIzaSyA7tGq5_OGeRARVbrKhm9lZvUjhgd-ncU4'
        
        #loop through registered id then send messages to registered devices
        reg_ids = GCMClientRegID.query()
        status = ''
        if reg_ids.count() > 0:
            for reg_id in reg_ids:
                params = {}
                params['data'] = {'message': 'receiver: ' + reg_id.user_name + ' ; sender: Gogistics Ltd.'}
                params['registration_ids'] = [reg_id.reg_id]
                
                json_parame = json.dumps(params)
                result = urlfetch.fetch(url = "https://android.googleapis.com/gcm/send",
                                  payload = json_parame,
                                  method=urlfetch.POST,
                                  headers = {'Content-Type': 'application/json' , 'Authorization':'key=' + API_KEY})
                status = result.content
        ajax_response = {'status':status}
        self.response.out.headers['Content-Type'] = 'text/json'
        self.response.out.write(json.dumps(ajax_response))
    
#dispatchers
app = webapp2.WSGIApplication([('/gcm_reg_id_handler', GCMReceiveRegIDHandler),('/gcm_send_message', GCMSendHandler)], debug =True)
        
#log 
logging.getLogger().setLevel(logging.DEBUG)
        