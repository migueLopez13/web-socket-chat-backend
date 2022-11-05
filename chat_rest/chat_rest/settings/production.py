from .base import *

DEBUG = env('DEBUG_PROD')

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_PROD_NAME'),
        'USER': env('POSTGRESQL_PROD_USER'),
        'PASSWORD': env('POSTGRESQL_PROD_PASS'),
        'HOST': env('POSTGRESQL_PROD_HOST'),
        'PORT': env('POSTGRESQL_PROD_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
