from django.test import TestCase
from rest_framework.reverse import reverse_lazy
from django_auth2.tests.base import BaseWithoutLoginMixin


class RegisterTest(BaseWithoutLoginMixin, TestCase):
    url = reverse_lazy('register')
