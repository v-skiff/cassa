from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'main/index.html')


class LoginView(LoginView):
    success_url = 'index'
    template_name = 'main/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'login'
    # template_name = 'main/logout.html'

