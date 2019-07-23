from .base import *

SECRET_KEY = "*HO;gua,B)O@tR8c;MmbA:B^tP}NNy8{c`hd9|TVYV;'3m6Zqx0Lhb_)B1vgIrQa"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"rest_framework",
	"webpack_loader",
	"frontend",
]

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",

]

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": "project.db",
	}
}

REST_FRAMEWORK = {}

WEBPACK_LOADER = {
	"FRONTEND": {
		"CACHE": not DEBUG,
		"BUNDLE_DIR_NAME": "frontend-bundle/", # must end with slash
		"STATS_FILE": os.path.join(ROOT_DIR, "frontend-stats.json"),
		"POLL_INTERVAL": 0.1,
		"TIMEOUT": None,
		"IGNORE": [".+\.hot-update.js", ".+\.map"]
	},
}
