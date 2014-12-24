'''
Created on Dec 24, 2014

@author: Alan Tai
'''

class KeyValuePairsGeneral():
    """ general key and value pair """
    def __init__(self):
        self.config_setting = {
                               'webapp2_extras.sessions': {'secret_key': 'b4RiUe~53!kGt3t34ty5y5-5&u90u1$%Y$%~e0.+54=954094309fewt3i-AqFB!.*^OHS$u2cNwOQGG',  # secret key is just a combination of random character which is better to be unguessable; user can create whatever they want
                                                           'cookie_name' : 'gogistics-winever-session',
                                                           'session_max_age' : 86400,
                                                           'cookie_args' : {'max_age' : 86400,
                                                                            'httponly' : True},} 
                               }