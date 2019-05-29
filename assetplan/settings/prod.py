from .base import *


#overide soometings here


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

    },
        'NAME': 'gideon$assetplan',
        'USER':'gideon',
        'PASSWORD':'Chirchir1',
        'HOST':'gideon.mysql.pythonanywhere-services.com',
        'PORT': ''

    }
    
}