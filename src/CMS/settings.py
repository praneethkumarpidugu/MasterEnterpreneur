"""
Django settings for CMS project.

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

SECRET_KEY = 'p-+_6ohnxln%g$jlzhj!w)vcm2m!w6q!te@qt!=w+*^_uko94x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


FULL_DOMAIN_NAME = 'http://wwww.masterentrepreneur.com'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'accounts',
    'analytics',
    'billing',
    'comments',
    'notifications',
    'videos',
)

CRISPY_TEMPLATE_PACK = "bootstrap3"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

ROOT_URLCONF = 'CMS.urls'

WSGI_APPLICATION = 'CMS.wsgi.application'

LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'accounts.MyUser'

RECENT_COMMENT_NUMBER = 10

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_dirs"),
    #'/var/www/static/',
)

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")

BRAINTREE_MERCHANT_ID = "85rcwqpqqj3hbn98"
BRAINTREE_PUBLIC_KEY = "j5d5khw4qp3j6jpg"
BRAINTREE_PRIVATE_KEY = "a8dde433bb2920067b3dccb5abb82274"

import dj_database_url
DATABASES['default'] = dj_database_url.config()

#Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']