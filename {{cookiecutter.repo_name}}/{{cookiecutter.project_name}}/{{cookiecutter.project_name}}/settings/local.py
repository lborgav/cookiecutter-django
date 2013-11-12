########## Settings for local use
from .base import *


########## DEBUG CONFIG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIG


########## EMAIL CONFIG
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
########## END EMAIL CONFIG


########## DATABASE CONFIG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': normpath(join(PROJECT_ROOT, 'database.db')),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
########## END DATABASE CONFIG


########## INTERNAL_IPS CONFIG
INTERNAL_IPS = ('127.0.0.1',)
########## END INTERNAL_IPS CONFIG


########## DEBUG_TOOLBAR_PANELS CONFIG
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
########## END DEBUG_TOOLBAR_PANELS CONFIG


INSTALLED_APPS += (
	'debug_toolbar', # Debug Toolbar
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
