from .base import *

import os

SECRET_KEY = '@i!@dw@9^x+lwpoa+kshoske7p+3!6qqjud8en_8q$lpz=-@k0'

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jmad_local',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        'ATOMIC_REQUESTS': True
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
