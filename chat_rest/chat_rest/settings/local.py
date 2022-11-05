from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG_DEV')

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_DEV_NAME'),
        'USER': env('POSTGRESQL_DEV_USER'),
        'PASSWORD': env('POSTGRESQL_DEV_PASS'),
        'HOST': env('POSTGRESQL_DEV_HOST'),
        'PORT': env('POSTGRESQL_DEV_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
