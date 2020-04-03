import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import resolve
import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from .models import Tool, CustomerInfo, Message


'''
THIS IS THE FEE WHEN A USER IS LATE RETURNING AN ITEM.  UPDATE IT HERE
'''
LATE_FEE = 5
'''
THIS IS THE NUMBER OF DAYS A SUBSCRIPTION PAYS FOR.  UPDATE IT HERE
'''
SUB_DAYS = 30


def index(request):  # Main page
    context = {}
    return render(request, 'Toolshop/index.html', context)


def projects_page(request):
    context = {}
    return render(request, 'Toolshop/projects.html', context)


def tools_page(request):
    tools_list = Tool.objects.order_by('category')
    context = {
        'tools_list': tools_list
    }
    return render(request, 'Toolshop/tools.html', context)


def contact_page(request):
    context = {}
    return render(request, 'Toolshop/contact.html', context)


def login_page(request):
    context = {}
    return render(request, 'Toolshop/login.html', context)


@login_required
def account_page(request):
    user = request.user
    tools_list = Tool.objects.filter(who_checked_out__contains=user.username)
    context = {
        'user': user,
        'tools_list': tools_list
    }
    return render(request, 'Toolshop/account.html', context)


@login_required
def reservation_page(request):
    tools_list = Tool.objects.order_by('category')
    context = {
        'tools_list': tools_list
    }
    return render(request, 'Toolshop/reservation.html', context)


@login_required
def reservation_page_specific(request, contains):  # This page has the results trimmed down by a search query
    if request.POST.get('query') is not None:
        contains = request.POST.get('query')
    tools_list = Tool.objects.filter(name__contains=contains).order_by('category')
    context = {
        'tools_list': tools_list
    }
    return render(request, 'Toolshop/reservation.html', context)

@login_required
def make_reservation(request, id):
    context = {}
    current_user = get_object_or_404(CustomerInfo, user=request.user)
    if current_user.current_outstanding_balance > 0 or not current_user.this_period_paid:
        return render(request, 'Toolshop/fees_overdue.html', context)
    tool = get_object_or_404(Tool, pk=id)
    tool.is_checked_out = True
    tool.times_checked_out += 1
    tool.date_checked_out = timezone.now()
    tool.who_checked_out = request.user.username
    current_user.num_currently_checked_out += 1
    tool.save()
    current_user.save()

    return render(request, 'Toolshop/redirect.html', context)


def update_user_info(request):
    user = request.user
    first_name = request.POST.get('firstName')
    last_name = request.POST.get('lastName')
    address = request.POST.get('address')
    email_address = request.POST.get('email')
    password_1 = request.POST.get('psw')
    password_2 = request.POST.get('psw-repeat')

    if password_1 != password_2:
        return HttpResponseRedirect(reverse('Toolshop:updateError'))
    elif first_name is None or last_name is None or address is None or email_address is None or password_1 is None:
        return HttpResponseRedirect(reverse('Toolshop:updateError'))
    elif first_name == "" or last_name == "" or address == "" or email_address == "" or password_1 == "":
        return HttpResponseRedirect(reverse('Toolshop:updateError'))
    elif len(first_name) > 30 or len(last_name) > 30 or len(email_address) > 50:
        return HttpResponseRedirect(reverse('Toolshop:updateError'))
    elif len(password_1) < 8 or len(password_1) > 30:
        return HttpResponseRedirect(reverse('Toolshop:updateError'))

    user.first_name = first_name
    user.last_name = last_name
    user.email = email_address
    user.address = address
    user.set_password(password_1)

    user.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('Toolshop:redirect'))


def submit_message(request):
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    email_address = request.POST.get('emailAddress')
    subject = request.POST.get('subject')
    message = request.POST.get('textBody')

    if first_name is None or last_name is None or email_address is None or subject is None or message is None:
        return HttpResponseRedirect(reverse('Toolshop:error'))
    elif first_name == "" or last_name == "" or email_address == "" or subject == "" or message == "":
        return HttpResponseRedirect(reverse('Toolshop:error'))
    elif len(first_name) > 30 or len(last_name) > 30 or len(email_address) > 50:
        return HttpResponseRedirect(reverse('Toolshop:error'))
    elif len(subject) > 100 or len(message) > 1000:
        return HttpResponseRedirect(reverse('Toolshop:error'))

    new_message = Message(first_name=first_name, last_name=last_name,
                          email=email_address, subject=subject,
                          message=message)
    new_message.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('Toolshop:redirect'))


def submission_error(request):
    context = {}
    return render(request, 'Toolshop/submission_error.html', context)


def update_error(request):
    context = {}
    return render(request, 'Toolshop/update_error.html', context)


def redirection_page(request):
    context = {}
    return render(request, 'Toolshop/redirect.html', context)


@permission_required('admin.can_add_log_entry')
def database_upload(request):
    template = "Toolshop/database_upload.html"
    prompt = {
        'order': 'Order of CSV should be category, name, value, quantity, on-hand, checked-out'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        print(int(column[3]))
        for i in range(int(column[3])):
            print("creating " + column[1])
            created = Tool(
                category=column[0],
                name=column[1],
                cost=column[2],
                times_checked_out=0
            )
            created.save()
    context = {

    }
    return render(request, template, context)


'''
THESE ARE THE EMPLOYEE VIEWS.
THIS IS A DIFFERENT PART OF THE WEBSITE, ONLY ACCESSIBLE BY EMPLOYEES
'''


@permission_required('user.is_staff')
def reports_main(request):
    context = {}
    return render(request, 'Toolshop/reports_main.html', context)


@permission_required('user.is_staff')
def reports_users(request):
    users_list = User.objects.all()
    context = {
        'users_list': users_list,
    }
    return render(request, 'Toolshop/reports_users.html', context)


@permission_required('user.is_staff')
def specific_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        "user": user,
    }
    return render(request, 'Toolshop/reports_specificuser.html', context)


@permission_required('user.is_staff')
def specific_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    context = {
        "tool": tool,
    }
    return render(request, 'Toolshop/reports_specifictool.html', context)


@permission_required('user.is_staff')
def reports_tools(request, sort_by):
    if sort_by == "checked_out":
        tools_list = Tool.objects.filter(is_checked_out=True)
    elif sort_by == "popularity":
        tools_list = Tool.objects.order_by("-times_checked_out")
    else:
        tools_list = Tool.objects.all()

    context = {
        'tools_list': tools_list,
    }
    return render(request, 'Toolshop/reports_tools.html', context)


@permission_required('user.is_staff')
def check_in_page(request):
    tools_list = Tool.objects.filter(is_checked_out=True)
    context = {
        'tools_list': tools_list,
    }
    return render(request, 'Toolshop/reports_checkin.html', context)


@permission_required('user.is_staff')
def add_tool_page(request):
    context = {}
    return render(request, 'Toolshop/reports_payfees.html', context)


@permission_required('user.is_staff')
def check_in(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    current_user = get_object_or_404(CustomerInfo, user=request.user)
    tool.is_checked_out = False
    tool.date_checked_out = None
    tool.who_checked_out = ""
    tool.save()
    if tool.is_overdue():
        current_user.current_outstanding_balance += LATE_FEE
    current_user.num_currently_checked_out -= 1
    current_user.save()
    message = "Tool successfully checked-in! Redirecting..."
    context = {
        "message": message,
    }
    return render(request, 'Toolshop/reports_redirect.html', context)


@permission_required('user.is_staff')
def pay_fee_page(request):
    users_list = User.objects.all().order_by('-customerinfo__current_outstanding_balance',
                                             'customerinfo__this_period_paid')
    context = {
        'users_list': users_list,
    }
    return render(request, 'Toolshop/reports_payfees.html', context)


@permission_required('user.is_staff')
def pay_fee(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.customerinfo.current_outstanding_balance = 0
    user.customerinfo.save()
    message = "Outstanding Fees successfully paid."
    context = {
        "message": message,
    }
    return render(request, 'Toolshop/reports_redirect.html', context)


@permission_required('user.is_staff')
def pay_period(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.customerinfo.this_period_paid = True
    user.customerinfo.date_paid_until = timezone.now() + timedelta(days=SUB_DAYS)
    user.customerinfo.save()
    message = "This period successfully paid."
    context = {
        "message": message,
    }
    return render(request, 'Toolshop/reports_redirect.html', context)

