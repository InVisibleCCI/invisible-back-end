"""
Django settings for invisible_backend project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

import environ
from algoliasearch.search_client import SearchClient

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env_variable = os.environ.get('PYTHON_ENVIRONMENT', 'prod').lower()
environ.Env.read_env(env_file=f'{BASE_DIR}/invisible_backend/environments/.env_{env_variable}')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+bsh^v%)*_och*80q9yz+p(63v2$kdvrhc1*d#hibrl=ec47&t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = list(default_headers) + ["LATITUDE", "LONGITUDE"]
GEOCODE_APP_NAME = 'invisible_api'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_crontab',
    'corsheaders',
    'django.contrib.gis',

    'common',
    "core",
    'event',
    'merchant'
]
AUTH_USER_MODEL = 'core.User'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'invisible_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['common/mails/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'invisible_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env.str('DATABASE_NAME', 'invisible-db'),
        'USER': env.str('DATABASE_USER', 'postgres'),
        'PASSWORD': env.str('DATABASE_PASSWORD', 'password'),
        'HOST': env.str('DATABASE_HOST', 'db'),
        'PORT': env.int('DATABASE_PORT', 5432)
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CRONTAB_COMMAND_PREFIX = '. $HOME/.bash_profile &&'
CRONTAB_COMMAND_SUFFIX = '2>&1'

# cronjob
CRONJOBS = [
    ('0 0,12 * * *', 'event.services.algolia_service.save_events_to_algolia', '>> /tmp/scheduled_job.log 2>&1')
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALGOLIA_CLIENT = SearchClient.create(env.str('ALGOLIA_APPLICATION_ID'), env.str('ALGOLIA_API_KEY'))
ALGOLIA_INDEX = ALGOLIA_CLIENT.init_index(env.str('ALGOLIA_INDEX'))

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30)
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'invisible.ovh@gmail.com'
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', '')
