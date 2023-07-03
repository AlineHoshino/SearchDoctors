import os
from .settings import *

DEBUG = True

SECRET_KEY = '5uhs6c2r@#8tq6o5!o1+zlhxhn)h0797tbpm83ig%g8o6bcvy$'

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
