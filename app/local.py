from .settings import *
import os

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'HOST': os.environ['POSTGRES_HOST'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'PORT': os.environ['POSTGRES_PORT'],
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG = True

ALLOWED_HOSTS = ['*']

# TODO-specific settings
TODO_STAFF_ONLY = False
TODO_DEFAULT_LIST_SLUG = 'tickets'
TODO_DEFAULT_ASSIGNEE = None
TODO_PUBLIC_SUBMIT_REDIRECT = '/'
