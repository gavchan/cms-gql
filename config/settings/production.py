# Production settings

from config.settings.common import *
import yaml

print("Using production settings")

# Read secret key from file
with open('dj_prod.key') as f:
    SECRET_KEY = f.read().strip()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

with open('config/db_settings_prod.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    cms_db = data['cms_db'][0]

DATABASE_ROUTERS = ['config.db_router.CmsDbRouter',]
DATABASE_APPS_MAPPING = {
  'cmsinv': 'cms_db',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'cms_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': cms_db['name'],
        'USER': cms_db['user'],
        'PASSWORD': cms_db['password'],
        'HOST': cms_db['host'],
        'PORT': cms_db['port'],
    },
}
