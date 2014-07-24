'''
Created on Jul 23, 2014

@author: Alan Tai
@description: brief description of using gcm handlers
'''
import logging
from handlers_gcm.handler_gcm import GCMMessage, GCMConnection

push_token = 'YOUR_PUSH_TOKEN'
android_payload = {'your-key': 'your-value'}

gcm_message = GCMMessage(push_token, android_payload)
gcm_conn = GCMConnection()

#
logging.info("Attempting to send Android push notification %s to push_token %s." % (repr(android_payload), repr(push_token)))
gcm_conn.notify_device(gcm_message)