import datetime

from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    times_checked_out = models.IntegerField()
    cost = models.IntegerField()
    condition = models.TextField(blank=True)  # Blank here means "Can be blank" sometimes.

    is_checked_out = models.BooleanField(default=False)
    date_checked_out = models.DateTimeField(blank='true')  # Blank here means "Can be blank" sometimes.
    who_checked_out = models.CharField(max_length=100, blank=True)  # Blank here means "Can be blank" sometimes.

    def __str__(self):
        return self.name
