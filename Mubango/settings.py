"""
Django settings for Mubango project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from decouple import config
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "social_django",
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_countries",
    "debug_toolbar",
    "phonenumber_field",
    "address",
    "account.apps.AccountConfig",
    "common",
    "business",
    "event.apps.EventConfig",
    "offer.apps.OfferConfig",
    "ad",
    "review",
    "core",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "Mubango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",  # <--
                "social_django.context_processors.login_redirect",  # <--
                "account.get_user_state_context_processor.get_user_state",
            ],
        },
    },
]

WSGI_APPLICATION = "Mubango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USERNAME"),
        "PASSWORD": config("DATABASE_PASSWORD"),
        "HOST": "localhost",  # Or an IP Address that your DB is hosted on
        "PORT": "3306",
        "ATOMIC_REQUESTS": True,
        "OPTIONS": {
            "sql_mode": "traditional",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)


AUTHENTICATION_BACKENDS = (
    "social_core.backends.linkedin.LinkedinOAuth2",
    "social_core.backends.google.GoogleOpenId",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.google.GoogleOAuth",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/mb/static/"
STATICFILES_DIRS = (
    os.path.join(
        BASE_DIR, "static"
    ),  # do not comment this line out as it renders the static files
)
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/upload/")
MEDIA_URL = os.path.join(BASE_DIR, "static/media/upload/")
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
X_FRAME_OPTIONS = "ALLOWALL"
GOOGLE_API_KEY = config("GOOGLE_API_KEY")
SOCIAL_AUTH_URL_NAMESPACE = "social"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/mb/account/home"
LOGOUT_URL = "logout"
LOGOUT_REDIRECT_URL = "login"
SOCIAL_AUTH_FACEBOOK_KEY = config("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = config("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", "user_link"]  # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {  # add this
    "fields": "id, name, email, picture.type(large), link"
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [  # add this
    ("name", "name"),
    ("email", "email"),
    ("picture", "picture"),
    ("link", "profile_url"),
]

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = config("SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY")  # Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = config(
    "SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET"
)  # Client Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ["r_emailaddress", "r_liteprofile"]
SOCIAL_AUTH_FIELD_SELECTORS = [
    "email-address",
]
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = [
    "email-address",
    "formatted-name",
    "public-profile-url",
    "picture-url",
]
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ("id", "id"),
    ("formattedName", "name"),
    ("emailAddress", "email_address"),
    ("pictureUrl", "picture_url"),
    ("publicProfileUrl", "profile_url"),
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/userinfo.email",
]
RABBITMQ_BROKER_URL = config("BROKER_URL")
RABBITMQ_USERNAME = config("BROKER_USERNAME")
RABBITMQ_PASSWORD = config("BROKER_PASSWORD")
RABBITMQ_PORT = config("BROKER_PORT", default="5672")
RABBITMQ_VHOST = config("BROKER_VHOST", default="pbp_main")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")
CELERY_BROKER_URL = (
    f"pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@"
    f"{RABBITMQ_BROKER_URL}/{RABBITMQ_VHOST}"
)

BROKER_URL = (
    f"pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@"
    f"{RABBITMQ_BROKER_URL}/{RABBITMQ_VHOST}"
)
