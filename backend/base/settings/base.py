import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")
BACKEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "../"))
ROOT_DIR = os.path.abspath(os.path.join(BACKEND_DIR, "../"))

ROOT_URLCONF = "base.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [],
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

WSGI_APPLICATION = "base.wsgi.application"

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = "/media/"
STATIC_URL = "/static/"
