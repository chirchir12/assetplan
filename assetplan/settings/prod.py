from .local import *
import os


#overide soometings here
SECRET_KEY ='^t@2&3nye6tn81!+u-ivq*no8&gb7r@!9#ua=83plfh5_%wagm'

ALLOWED_HOSTS = ['http://assetplan.co.ke','www.assetplan.co.ke', 'assetplan.co.ke', 'https://www.assetplan.co.ke/']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

    },
        'NAME':'gideon$assetplan',
        'USER':'gideon',
        'PASSWORD':'gID@123.!',
        'HOST':'gideon.mysql.pythonanywhere-services.com',
        'PORT': ''

    }
    
}