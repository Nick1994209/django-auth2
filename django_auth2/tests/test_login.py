from django.test import TestCase
from django.urls import reverse_lazy

from .base import BaseWithoutLoginMixin


class LoginTest(BaseWithoutLoginMixin, TestCase):
    url = reverse_lazy('login')
