from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile

EXEMPT_URLS = []
EXEMPT_URLS += [compile(expr.lstrip('/')) for expr in getattr(settings, 'LOGIN_EXEMPT_URLS', [])]


class LoginRequiredMiddleware:

    def process_request(self, request):

        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any([m.match(path) for m in EXEMPT_URLS]):
                login_url = settings.LOGIN_URL.rstrip('/') + '/?next_url={}'.format(path)
                return HttpResponseRedirect(login_url)
