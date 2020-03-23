from django.urls import path

from . import views

app_name = 'Toolshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account_page, name='account'),
    path('hammers/', views.hammers_page, name='hammers'),
    path('wrenches/', views.wrenches_page, name='wrenches'),
    path('drills/', views.drills_page, name='drills'),
    path('ohMy/', views.oh_my_page, name='ohMy'),
]
