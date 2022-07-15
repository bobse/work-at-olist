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

DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'], conn_max_age=600, ssl_require=True)}



