from .base import * 

#  SECRET_KEY = 'django-insecure-pzb@s^+lz!3%wb62^oj84vkp0&)k#g14f2$^x2!^oxhf%h^27u'

with open(os.path.join(BASE_DIR,'secret.txt')) as f :
    SECRET_KEY= f.read().strip()

DEBUG = True 

ALLOWED_HOSTS = ['*'] 

INSTALLED_APPS += [
   'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'customer',
    'product',
    'restapi',
    'corsheaders',
]

CORS_ORIGIN_ALLOW_ALL = True

