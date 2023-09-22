from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

import os


from dotenv import load_dotenv

load_dotenv(".env")

SECRET_KEY = os.environ.get("SECRET_KEY", None)

DEBUG = os.environ.get("DEBUG", False)


ALLOWED_HOSTS = list(str(os.environ.get("ALLOWED_HOSTS")).split(", "))


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework", #

    "django_extensions", #

    "users", #
    "products", #
    "orders", #
    "shifts", #
    "financials", #
    "employees", #

]


AUTH_USER_MODEL = "users.Person"

AUTHENTICATION_BACKENDS = [
    'users.authentication.CustomUserAuthBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EspressoToGo.urls'

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

WSGI_APPLICATION = 'EspressoToGo.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": str(os.environ.get("DATABASE_NAME")),
        "USER": str(os.environ.get("DATABASE_USER")),
        "PASSWORD": str(os.environ.get("DATABASE_PASSWORD")),
        "HOST": str(os.environ.get("DATABASE_HOST")),
        "PORT": int(os.environ.get("DATABASE_PORT")),
        # 'TEST': {
        #     'NAME': '',
        # },
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
