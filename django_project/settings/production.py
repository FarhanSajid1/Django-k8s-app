from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE', ),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'PORT': os.environ.get('PGPORT'),
        'HOST': os.environ.get('PGHOST')
    }
}

ALLOWED_HOSTS = [
    '*'
]
# static/media urls and roots for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# USE_S3 = True
# USE_S3 = os.environ.get('USE_S3', True)
# if USE_S3:
#     # aws settings
#     INSTALLED_APPS += ['storages']
#     AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#     AWS_S3_REGION_NAME = 'us-east-2'
#     AWS_S3_FILE_OVERWRITE = False
#     AWS_DEFAULT_ACL = None
#
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     # this is to get the static files
#     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     AWS_S3_SIGNATURE_VERSION = 's3v4'
#     SENDFILE_BACKEND = 'sendfile.backends.simple'
#
# else:
#     MEDIA_ROOT = '/var/www/blog/media/'
#     MEDIA_URL = '/media/'




