import datetime

from django.contrib.auth.models import User
from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    times_checked_out = models.IntegerField()
    cost = models.IntegerField()
    condition = models.TextField(blank=True)  # Blank here means "Can be blank" sometimes.

    is_checked_out = models.BooleanField(default=False)
    date_checked_out = models.DateTimeField(blank=True, null=True)  # Blank\null here means "Can be blank" sometimes.
    who_checked_out = models.CharField(max_length=100, blank=True)  # Blank here means "Can be blank" sometimes.

    def __str__(self):
        return self.name


class CustomerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=25)
    address = models.TextField()

    this_period_paid = models.BooleanField(default=False)
    date_paid_until = models.DateTimeField(blank=True, null=True)
    num_currently_checked_out = models.PositiveIntegerField(default=0)
    current_outstanding_balance = models.PositiveIntegerField(blank=True, default=0)
