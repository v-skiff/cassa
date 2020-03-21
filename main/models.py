from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True, verbose_name="Имя")
    phone = models.CharField(max_length=250, blank=True, null=True, verbose_name="Телефон")
    email = models.CharField(max_length=250, blank=True, null=True, verbose_name="Email")
    note = models.TextField(blank=True, null=True, verbose_name="Заметка")
    is_archived = models.BooleanField(default=False, verbose_name="Архивировать?")

    def __str__(self):
        return self.name