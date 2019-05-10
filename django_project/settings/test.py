from .base import *
import os

'''Database parameters!'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('postgres', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASS', 'postgres_password'),
        'PORT': '5432',
        'HOST': 'postgres'
    }
}

USE_S3 = True
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/blog/static/'


if USE_S3:
    # aws settings
    INSTALLED_APPS += ['storages']
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'us-east-2'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    SENDFILE_BACKEND = 'sendfile.backends.simple'
else:
    MEDIA_ROOT = '/var/www/blog/media/'
    MEDIA_URL = '/media/'
