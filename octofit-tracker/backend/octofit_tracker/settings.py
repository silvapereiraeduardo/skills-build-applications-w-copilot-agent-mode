import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-secret'

DEBUG = True

ALLOWED_HOSTS = ['*']
# Add Codespace host if available (e.g. <CODESPACE_NAME>-8000.app.github.dev)
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    codespace_host = f"{codespace_name}-8000.app.github.dev"
    ALLOWED_HOSTS.insert(0, codespace_host)
    # Trust the codespace origin for CSRF when present
    CSRF_TRUSTED_ORIGINS = [f"https://{codespace_host}"]
else:
    CSRF_TRUSTED_ORIGINS = []

# For development in Codespaces, avoid forcing SSL redirects
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'djongo',
    'rest_framework',
    'octofit_app',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'octofit_tracker.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'octofit_tracker.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017'),
        }
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS - allow all during development
CORS_ALLOW_ALL_ORIGINS = True

