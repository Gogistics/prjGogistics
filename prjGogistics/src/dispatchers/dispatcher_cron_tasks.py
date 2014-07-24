'''
Created on Jul 24, 2014

@author: user
'''
import webapp2
import logging
from google.appengine.api import taskqueue

class GCMCronTaskHandler(webapp2.RequestHandler):
    def get(self):
        taskqueue.add(url = '/gcm_send_message')
    
#dispatchers
app = webapp2.WSGIApplication([('/cron_tasks_gcm_handler', GCMCronTaskHandler)], debug = True)

#log 
logging.getLogger().setLevel(logging.DEBUG)