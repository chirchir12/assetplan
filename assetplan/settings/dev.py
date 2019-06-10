from .local import *

ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = os.environ['SECRET_KEY']

EMAIL_HOST =os.environ['EMAIL_HOST']
EMAIL_PORT =os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD =os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

    },
        'NAME': os.environ['DATABASE_NAME'],
        'USER':os.environ['DATABASE_USER'],
        'PASSWORD':os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': ''

    }
    
}