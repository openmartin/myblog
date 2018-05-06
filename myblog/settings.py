"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mcn095fn00qgnt!i^$a4ymf4n-++u5u^90k3ih2y58ac!6+n!n'

IN_PRODUCTION = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

if IN_PRODUCTION == True:
	DEBUG = False
	TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


# Application definition

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.admin',
  'django.contrib.sites',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.contenttypes',
  'django_comments',
  'django.contrib.sitemaps',
  'mptt',
  'tagging',
  'zinnia_bootstrap',
#  'zinnia_html5',
  'zinnia',
  'zinnia_markitup',
  'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
	#'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'

# Template
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
		'USER': 'blog',
		'PASSWORD': '7QaUCU7E3TLbCsS3',
		'HOST': '127.0.0.1',
		'PORT': '3307',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
gettext = lambda s: s

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'static'

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# zinnia config
# ZINNIA_MARKUP_LANGUAGE = 'restructuredtext'
ZINNIA_MARKUP_LANGUAGE = 'markdown'

ZINNIA_MARKDOWN_EXTENSIONS = \
['markdown.extensions.extra','markdown.extensions.toc',
        'markdown.extensions.nl2br']

# ZINNIA_RESTRUCTUREDTEXT_SETTINGS = {'report_level': 'quiet'}
