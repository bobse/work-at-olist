from .base import *

"""
Django development settings for library project.

"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


INTERNAL_IPS = [
    '127.0.0.1'
]
# django toolbar
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS.append('debug_toolbar')

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
}

DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'], conn_max_age=600, ssl_require=False)}
