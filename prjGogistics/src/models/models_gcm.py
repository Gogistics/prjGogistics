'''
Created on Jul 23, 2014

@author: user
'''
from google.appengine.ext import ndb

class GCMClientRegID(ndb.Model):
    reg_id = ndb.StringProperty()
    user_name = ndb.StringProperty()
    created_date_time = ndb.DateTimeProperty(auto_now_add = True)