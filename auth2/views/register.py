from django.contrib import auth
from django.shortcuts import redirect, render
from django.views.generic import FormView
from auth2.forms import RegisterForm
from auth2 import utils
from auth2 import mails
from auth2.utils import RedirectActiveUser


class Register(RedirectActiveUser, FormView):
    form_class = RegisterForm
    template_name = "auth2/register/register.html"

    def form_valid(self, form):
        form.save()

        user = utils.get_user(username=form.cleaned_data['username'])
        user.is_active = False
        user.save()
        mails.send_activation_mail(self.request, user)

        # user_cache = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        #
        # auth.login(self.request, user_cache)
        return render(self.request, template_name='auth2/register/email_sended.html')

register = Register.as_view()