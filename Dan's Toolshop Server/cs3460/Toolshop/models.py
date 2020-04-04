import datetime

from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta
from django.utils import timezone


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

    def get_due_date(self):
        if self.date_checked_out is None or self.date_checked_out == "":
            return False
        return self.date_checked_out + timedelta(days=7)

    def is_overdue(self):
        if self.date_checked_out is None or self.date_checked_out == "":
            return False
        return self.date_checked_out + timedelta(days=7) < timezone.now()

    def is_condition_listed(self):
        if self.condition == "":
            return False
        return True


class CustomerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=25)
    address = models.TextField()

    this_period_paid = models.BooleanField(default=False)
    date_paid_until = models.DateTimeField(blank=True, null=True)
    num_currently_checked_out = models.PositiveIntegerField(default=0)
    current_outstanding_balance = models.PositiveIntegerField(blank=True, default=0)

    def is_address_listed(self):
        if self.address == "":
            return False
        return True

    def update_user_status(self):
        if self.date_paid_until is None or self.date_paid_until == "":
            return
        if self.date_paid_until < timezone.now():
            self.this_period_paid = False
            self.date_paid_until = None
            self.save()
            return
        return


class Message(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject
