from .base import *
import dj_database_url
from decouple import config

DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = config('SECRET_KEY', default='3sc8v@mxzfssp=vfbh!k=@4t!u9lwlgqx&*^o%v@l3$9z)-le)')

if config('DJANGO_PRODUCTION_ENV', default=False, cast=bool):
    from .base import *