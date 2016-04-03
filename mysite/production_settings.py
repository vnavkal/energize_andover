import os


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'development')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite',
        'USER': os.environ.get('db_user'),
        'PASSWORD': os.environ.get('db_password'),
        'HOST': os.environ.get('db_uri'),
        'PORT': os.environ.get('db_port')
    }
}
