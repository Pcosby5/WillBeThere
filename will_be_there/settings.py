"""
Django settings for will_be_there project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
import dotenv
import corsheaders

from django.core.mail import send_mail
# from django.contrib.auth.models import User


dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =["*"]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_ALL_ORIGIN = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://willbethere.vercel.app',
]


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'knox',
    'api',
    'will_be_there',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'crispy_forms',
    #'crispy_bootstrap4',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'will_be_there.urls'

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

WSGI_APPLICATION = 'will_be_there.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


database_url = os.environ.get("DATABASE_URL")
# # # # Set default database configuration

DATABASES = {
    'default': dj_database_url.parse(database_url)
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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'https://willbethere.vercel.app/dashboard'

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',)
# }

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['knox.auth.TokenAuthentication',
        # Add other authentication classes if needed
    ],
}

AUTH_USER_MODEL = 'api.User'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.elasticemail.com'
EMAIL_PORT = 465  # or 587
EMAIL_HOST_USER = 'pcosby50@gmail.com'  # Replace with your Elastic Email username
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD_1")
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'pcosby50@gmail.com'  # Replace with your email address




def send_password_reset_email(request, user_id):
    from django.contrib.auth.models import User  # Import User model locally within the function
    try:
        user = User.objects.get(pk=user_id)
        email_subject = "Password Reset Request"
        message = "Hi {},\n\nYou have requested a password reset. Please click on the link below to reset your password:\n\nLink here".format(user.first_name)
        send_mail(
            email_subject,
            message,
            'pcosby50@gmail.com',  # Sender's email
            [user.email],           # List of recipients - in this case, just the user
            fail_silently=False,
        )
    except User.DoesNotExist:
        # Handle error if user does not exist
        pass


# LOGIN_REDIRECT_URL = '/'
# ACCOUNT_LOGIN_REDIRECT_URL = '/'  # Specifically for Django Allauth
# ACCOUNT_LOGOUT_REDIRECT_URL = '/'
