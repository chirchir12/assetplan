from .local import *
import os

DEBUG=False
#overide soometings here
SECRET_KEY =os.getenv("SECRET_KEY")

EMAIL_HOST =os.getenv('EMAIL_HOST')
EMAIL_PORT =os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS =os.getenv('EMAIL_USE_TLS')

ALLOWED_HOSTS = ['http://assetplan.co.ke','www.assetplan.co.ke', 'assetplan.co.ke', 'https://www.assetplan.co.ke/']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

    },
        'NAME':os.getenv("DATABASE_NAME"),
        'USER':os.getenv("DATABASE_USER"),
        'PASSWORD':os.getenv("DATABASE_PASSWORD"),
        'HOST':os.getenv("DATABASE_HOST"),
        'PORT': ''

    }
    
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static"),
    
]

STATIC_ROOT = '/home/gideon/static_cdn/static-root'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/gideon/static_cdn/media-root'