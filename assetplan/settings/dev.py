from .base import *



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

    },
        'NAME': 'assetplan',
        'USER':'root',
        'PASSWORD':'Chirchir1.',
        'HOST':'localhost',
        'PORT': ''

    }
    
}