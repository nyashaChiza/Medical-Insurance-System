

import os
from pathlib import Path

from dotenv import load_dotenv
import loguru 

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")#"django-insecure-fq()c6k+g09#*ci@16o1ales8r$hvrvia#b+=8#_0o14rdo3)="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")
USE_MYSQL = os.getenv("USE_MYSQL")

ALLOWED_HOSTS = ['localhost', '127.0.0.1','.ngrok.io']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dashboard.apps.DashboardConfig",
    "claims.apps.ClaimsConfig",
    "certificates",
    "service_providers",
    
    #3rd party apps
    "crispy_forms",

]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "medical_insurance_system.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "medical_insurance_system.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if USE_MYSQL == "false":
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    }
    
if USE_MYSQL == "true" :

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv("MYSQL_DB_NAME"),
            "USER": os.getenv("MYSQL_DB_USER"),
            "PASSWORD": os.getenv("MYSQL_DB_PASSWORD"),
            "HOST": os.getenv("MYSQL_DB_HOST"),
            "PORT": os.getenv("MYSQL_DB_PORT")
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
DATASET_PATH = os.path.join(BASE_DIR, "claims/datasets")
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGER = loguru.logger


CERTIFICATE_TEMPLATE = f"{MEDIA_ROOT}/certificate_templates/Certificate of Service.docx"

GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
RELATIONSHIP_CHOICES = (('Single', 'Single'), ('Husband', 'Husband'), ('Wife','Wife'),('Brother','Brother'),('Sister','Sister'),('Aunt','Aunt'),('Grandmother','Grandmother'),('Uncle','Uncle'),('Grandfather','Grandfather'),('Nephew','Nephew'),('Niece','Niece'),('Other','Other'))
CAUSE_CHOICES = (('RTA','Road Traffic Accident'),('AAH','Accident At Home'),('AAW','Accident At Work'),('O','Other'))
CLASS_CHOICES = (('Fraud','Fraud'), ('Clean','Clean'),(None, None))

CSRF_TRUSTED_ORIGINS = ["https://*.ngrok.io"]