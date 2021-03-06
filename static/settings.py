import os
# Django settings for BrewMe project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'Aboleth',                      # Or path to database file if using sqlite3.
        'USER': 'wyattpj',                      # Not used with sqlite3.
        'PASSWORD': 'appstate',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/phillipsra1/dev/BrewMe/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    '/home/deployer/static',
    '/home/phillipsra1/dev/BrewMe/Home_Screen/static',
    '/home/phillipsra1/dev/BrewMe/Recipe/static',
    os.path.join(SITE_ROOT),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd08-@_47fz=z=s+ue^tii)^c&amp;g$*l-x-w*qj=ih29zdp(2@!qd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'BrewMe.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'BrewMe.wsgi.application'

TEMPLATE_DIRS = (
        '/home/phillipsra1/dev/BrewMe/Templates',
        '/home/phillipsra1/dev/BrewMe/Templates/User_Auth',
        '/home/phillipsra1/dev/BrewMe/Templates/Home_Screen',
        '/home/phillipsra1/dev/BrewMe/Templates/Recipe',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'User_Auth',
    'bootstrap_toolkit',
    'Recipe',
    'Home_Screen',
    'ajax_select',
    'haystack',
    #Not sure if i need this
    #'BrewMe_index',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#Site URL
#Change this to change the port you are working on
SITE_URL = 'http://66.169.77.204:8000'

# Static bootstrap urls
BOOTSTRAP_BASE_URL      = 'http://twitter.github.io/bootstrap/assets/'
BOOTSTRAP_CSS_URL       = 'http://bootswatch.com/united/bootstrap.min.css'
#BOOTSTRAP_CSS_BASE_URL  = BOOTSTRAP_BASE_URL + 'css/'
#BOOTSTRAP_CSS_URL       = BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
BOOTSTRAP_JS_BASE_URL   = BOOTSTRAP_BASE_URL + 'js/'

# Used by login_required decorator
LOGIN_URL = '/user/'

# Used by django-ajax-selects app
AJAX_LOOKUP_CHANNELS = {
        'Hop Variety' : {'model' : 'Recipe.Hops', 'search_field' : 'name'}
        }

#Haystack setup
HAYSTACK_SITECONF = 'BrewMe.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = '/home/wyattpj/dev/BrewMe/index'

#Haystack 2.0.0. We're using 1.2.7
"""HAYSTACK_CONNECTIONS = {
    'default' : {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH'  : os.path.join(os.path.dirname(__file__), 'whoosh_index'),    
        }
}"""
