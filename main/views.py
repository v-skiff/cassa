from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member, Payment, Report
from .forms import MemberForm, PaymentForm


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        balance = Report.get_balance()
        payments_count = Report.get_payments_count()
        member_count = Report.get_member_count()
        expenses_count = 0
        context = {
            'balance': balance,
            'payments_count': payments_count,
            'member_count': member_count,
            'expenses_count': expenses_count,
        }
        return render(request, 'main/index.html', context)


# Reports
class MainReport(View):
    def get(self, request):
        return render(request, 'main/main_report.html')


# Member
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


# Payment
class PaymentList(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'main/payment_list.html'


class PaymentDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        payment.delete()
        return redirect(reverse('payment_list'))


class PaymentUpdate(LoginRequiredMixin, UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'main/payment_update.html'
    success_url = reverse_lazy('payment_list')


class PaymentCreate(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'main/payment_create.html'
    success_url = reverse_lazy('payment_list')


# Authentication
class LoginView(LoginView):
    success_url = 'index'
    template_name = 'main/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'login'

