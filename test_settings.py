DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

INSTALLED_APPS = [
    'dillfield',
]

SECRET_KEY = 'local'

SILENCED_SYSTEM_CHECKS = ['1_7.W001']
