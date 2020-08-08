#production.pyは本番環境用です。
from .base import *

DEBUG = False
#DEBUG = True
try:
    from .local import *
except ImportError:
    pass

#add new for deploy
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
