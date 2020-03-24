from django.db import models
from django.db.models import Sum


class Member(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, verbose_name="Имя")
    phone = models.CharField(max_length=250, blank=True, null=True, verbose_name="Телефон")
    email = models.CharField(max_length=250, blank=True, null=True, verbose_name="Email")
    note = models.TextField(blank=True, null=True, verbose_name="Заметка")
    is_archived = models.BooleanField(default=False, verbose_name="Архивировать?")

    def __str__(self):
        return self.name


class Payment(models.Model):
    member = models.ForeignKey(Member, related_name='payments', on_delete=models.PROTECT, verbose_name="Участник")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Значение")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")

    def __str__(self):
        return str(self.value)


class Report:
    def get_balance():
        payments_total = Payment.objects.aggregate(Sum('value'))['value__sum']
        # expenses_total = Expense.objects.aggregate(Sum('value'))['value__sum']
        balance = payments_total - 0
        return balance

    def get_payments_count():
        return Payment.objects.all().count()

    def get_member_count():
        return Member.objects.all().count()