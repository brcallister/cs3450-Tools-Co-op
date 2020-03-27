from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = 'Toolshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account_page, name='account'),
    path('reserve/', views.reservation_page, name='reserve'),
    path('tools/', views.tools_page, name='tools'),
    path('projects/', views.projects_page, name='projects'),
    path('contact/', views.contact_page, name='contact'),
    path('redirect/', views.redirection_page, name='redirect'),
    path('database_upload', views.database_upload, name='database_upload'),
]
