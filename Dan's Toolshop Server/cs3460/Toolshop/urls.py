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

    # The employee-only section of the website
    path('Employee/', views.reports_main, name='reports_main'),
    path('Employee/users', views.reports_users, name='reports_users'),
    path('Employee/tools/<str:sort_by>', views.reports_tools, name='reports_tools'),
    path('Employee/check_in', views.check_in_page, name='check_in'),
    path('Employee/add_tool', views.add_tool_page, name='add_tool'),

    # Actions
    path('makeReservation/<int:id>', views.make_reservation, name='makeReservation'),
    path('submitMessage/', views.submit_message, name='submitMessage'),
    path('updateUserInfo/', views.update_user_info, name='update'),
    path('check_in_tool/<int:tool_id>', views.check_in, name='check_in_tool'),
    path('add_tool/', views.add_tool, name='add_tool'),

    # Misc urls
    path('redirect/', views.redirection_page, name='redirect'),
    path('database_upload', views.database_upload, name='database_upload'),
]
