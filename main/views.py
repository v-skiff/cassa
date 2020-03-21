from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member
from .forms import MemberForm


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'main/index.html')


class MemberList(LoginRequiredMixin, ListView):
    model = Member
    template_name = 'main/member_list.html'


class MemberDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        member = Member.objects.get(pk=pk)
        member.delete()
        return redirect(reverse('member_list'))


class MemberUpdate(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'main/member_update.html'
    success_url = reverse_lazy('member_list')


class MemberCreate(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'main/member_create.html'
    success_url = reverse_lazy('member_list')


class LoginView(LoginView):
    success_url = 'index'
    template_name = 'main/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'login'

