from .local import *
import os


#overide soometings here
SECRET_KEY = os.getenv("SECRET_KEY"),

ALLOWED_HOSTS = ['http://assetplan.co.ke','www.assetplan.co.ke', 'assetplan.co.ke', 'https://www.assetplan.co.ke/']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

    },
        'NAME':  os.getenv("DATABASE_NAME"),
        'USER':os.getenv("DATABASE_USER"),
        'PASSWORD':os.getenv("DATABASE_PASSWORD"),
        'HOST':os.getenv("DATABASE_HOST"),
        'PORT': ''

    }
    
}