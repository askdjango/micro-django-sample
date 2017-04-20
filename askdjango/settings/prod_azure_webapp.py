from .common import *

import pymysql
pymysql.install_as_MySQLdb()

DEBUG = False

INSTALLED_APPS += ['storages']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'HOST': os.environ.get('DB_HOST', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'NAME': os.environ.get('DB_NAME', ''),
    },
}

DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE', 'storages.backends.azure_storage.AzureStorage')

# 설정 / 액세스 키
AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', '')
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', '')
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', '')
