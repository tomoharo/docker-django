from .settings import *

DEBUG = False
ALLOWED_HOSTS = env.get_value('PROD_ALLOWED_HOSTS',list)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get_value('DATABASES_NAME',str),
        'USER': env.get_value('DATABASES_USER',str),
        'PASSWORD': env.get_value('DATABASES_PASSWORD',str),
        'HOST': env.get_value('DATABASES_HOST',str),   
        'PORT': '3309',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY',
        },
    }
}