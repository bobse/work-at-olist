from .base import *

"""
Django production settings for library project.

"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#TODO: confirm allowed hosts
ALLOWED_HOSTS = ['olistlibrary.herokuapp.com']

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

#TODO: replace with postgres for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

