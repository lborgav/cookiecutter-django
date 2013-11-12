########## Settings for production use
from .base import *


########## DEBUG CONFIG
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIG


########## EMAIL CONFIG
########## END EMAIL CONFIG


########## DATABASE CONFIG
DATABASES = {
    'default': {
        'ENGINE': '', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
########## END DATABASE CONFIG


INSTALLED_APPS += (
)


MIDDLEWARE_CLASSES += (
)
