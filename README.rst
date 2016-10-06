pip install django_auth2


INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django_auth2',
]

in User model add
    email = models.EmailField(unique=True, blank=False)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'someone@someorg.com'
EMAIL_HOST_PASSWORD = 'thepassword'
EMAIL_PORT = 587

password reset days in project.settings
    PASSWORD_RESET_TIMEOUT_DAYS = 1

View with name "index" for redirect (after authentication)



celery
<a>http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html</a>

settings must be in project.settings (or change auth2.celery get settings)
