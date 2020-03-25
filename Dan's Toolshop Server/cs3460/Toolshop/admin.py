from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import CustomerInfo

from .models import Tool


class CustomerInline(admin.StackedInline):
    model = CustomerInfo
    can_delete = False
    verbose_name_plural = 'Additional Info'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Tool)
