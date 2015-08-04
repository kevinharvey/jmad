import os

from .base import *

WSGI_APPLICATION = 'jmad.wsgi.application'


ALLOWED_HOSTS = [os.environ.get('SERVER_NAME')]


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


STATIC_ROOT = os.environ.get('STATIC_ROOT')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT')


EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


BROKER_URL = os.environ.get('BROKER_URL')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.environ.get('DJANGO_ERROR_LOG'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'jmad': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
