import os
import sys
import dj_database_url
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')

# Adicionar a tag dotenv
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Diz para o Django onde estão nossos aplicativos
APPS_DIR = str(os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, APPS_DIR)

# Avisos de segurança: mantenha esta chave secreta em segredo de produção
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Register',
]

# CORS Config
CORS_ORIGIN_ALLOW_ALL = True  
# CORS_ORIGIN_ALLOW_ALL como True, o que permite que qualquer site acesse seus recursos.
# Defina como False e adicione o site no CORS_ORIGIN_WHITELIST onde somente o site da lista acesse os seus recursos.

CORS_ALLOW_CREDENTIALS = False 

CORS_ORIGIN_WHITELIST = ['http://meusite.com',] # Lista.

if not DEBUG:
	SECURE_SSL_REDIRECT = True
	ADMINS = [(os.getenv('SUPER_USER'), os.getenv('EMAIL'))]
	SESSION_COOKIE_SECURE = True
	CSRF_COOKIE_SECURE = True 

# Application definition
DJANGO_APPS = [
	'apps.contas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

THIRD_APPS = [
    "corsheaders",
]

PROJECT_APPS = [
	'apps.base',
	'apps.pages',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django_session_timeout.middleware.SessionTimeoutMiddleware', # Timeout
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Cors
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'requestlogs.middleware.RequestLogsMiddleware', # Logs
    
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				# Apps
                'base.context_processors.context_social', 
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_USER_MODEL = "contas.MyUser"

# Lê a URL do banco de dados do .env
DATABASE_URL = os.getenv('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK={
    'EXCEPTION_HANDLER': 'requestlogs.views.exception_handler',
}

# Logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requestlogs_to_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
        },
    },
    'loggers': {
        'requestlogs': {
            'handlers': ['requestlogs_to_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

REQUESTLOGS = {
    # 'STORAGE_CLASS': 'requestlogs.storages.LoggingStorage',
    # 'ENTRY_CLASS': 'requestlogs.entries.RequestLogEntry',
    # 'SERIALIZER_CLASS': 'requestlogs.storages.BaseEntrySerializer',
    'SECRETS': ['password', 'token'],
    # 'ATTRIBUTE_NAME': '_requestlog',
    'METHODS': ('GET', 'PUT', 'PATCH', 'POST', 'DELETE'),
    # 'JSON_ENSURE_ASCII': True,
    # 'IGNORE_USER_FIELD': None,
    # 'IGNORE_USERS': [],
    # 'IGNORE_PATHS': None,
}

# SESSION_EXPIRE_SECONDS = 10 # minuts
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60
SESSION_TIMEOUT_REDIRECT = 'http://localhost:8000/contas/timeout/'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Boa_Vista'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/' 

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Menssages
from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
	constants.DEBUG: 'alert-danger',
	constants.SUCCESS: 'alert-success',
	constants.INFO: 'alert-info',
}
