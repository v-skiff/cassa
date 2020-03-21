from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    is_archived = models.BooleanField(default=False)