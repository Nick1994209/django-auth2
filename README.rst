### set in installed apps
<code><pre>
INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'auth2',
]
</pre></code>

##### add backend for email
<code>
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
</code>

#### your user
<code>
email = models.EmailField(unique=True, blank=False)
</code>

##### Email setup
<code><pre>
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'someone@someorg.com'
EMAIL_HOST_PASSWORD = 'thepassword'
EMAIL_PORT = 587
</pre></code>

##### password reset days in project.settings
<code>
PASSWORD_RESET_TIMEOUT_DAYS = 1
 </code> # one day for user can changed pas

#### view with name "index" (for redirect)

##celery
<a>
http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
</a>

settings must be in project.settings (or change auth2.celery get settings)

for launch
