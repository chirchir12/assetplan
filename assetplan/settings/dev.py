from .local import *

ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = '^t@2&3nye6tn81!+u-ivq*no8&gb7r@!9#ua=83plfh5_%wagm'
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