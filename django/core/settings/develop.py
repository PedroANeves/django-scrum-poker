import os

DEBUG = True

ALLOWED_HOSTS = ['localhost']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TKaVmY6Uzay9VgR9lH7aOKdpzVsTlGizClcFphcieHI'

CHANNEL_LAYERS={
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
     }
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
