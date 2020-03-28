from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = 'Toolshop'

urlpatterns = [
    # The main website pages
    path('', views.index, name='index'),
    path('account/', views.account_page, name='account'),
    path('reserve/', views.reservation_page, name='reserve'),
    path('reserve/<str:contains>', views.reservation_page_specific, name='reserve_spec'),
    path('tools/', views.tools_page, name='tools'),
    path('projects/', views.projects_page, name='projects'),
    path('contact/', views.contact_page, name='contact'),
    path('error/', views.submission_error, name='error'),
    path('updateError/', views.update_error, name='updateError'),

    # Actions
    path('makeReservation/<int:id>', views.make_reservation, name='makeReservation'),
    path('submitMessage/', views.submit_message, name='submitMessage'),
    path('updateUserInfo/', views.update_user_info, name='update'),


    # Misc urls
    path('redirect/', views.redirection_page, name='redirect'),
    path('database_upload', views.database_upload, name='database_upload'),
]
