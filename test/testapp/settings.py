# Django settings for testapp project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'testdb.sqlite',                      # Or path to database file if using sqlite3.
    }
}

LANGUAGE_CODE = 'en-us'
SITE_ID = 1

MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/media/static/'

LOGIN_REDIRECT_URL = '/profile/edit/'

ADMIN_MEDIA_PREFIX = '/media/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'qd@j3*it@3j2cgc#7t@m)^r1bnc53uam7o6u_+x$f5w3$b@3ix'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'testapp.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'pybb',
    'pytils',
    'registration',
    'sorl.thumbnail',
    'south',
    'pure_pagination',

)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'pybb.context_processors.processor',
)

AUTH_PROFILE_MODULE = 'pybb.Profile'

PYBB_TEMPLATE = "pybb/bootstrap_base.html"
ACCOUNT_ACTIVATION_DAYS=30

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
