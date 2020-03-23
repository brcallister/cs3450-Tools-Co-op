from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

#from .models import TOOLS CLASSES


def index(request):  # Main page
    context = {

    }
    return render(request, 'Toolshop/index.html', context)


def account_page(request):
    context = {

    }
    return render(request, 'Toolshop/account.html', context)


def hammers_page(request):
    context = {

    }
    return render(request, 'Toolshop/hammers.html', context)


def wrenches_page(request):
    context = {

    }
    return render(request, 'Toolshop/wrenches.html', context)


def drills_page(request):
    context = {

    }
    return render(request, 'Toolshop/drills.html', context)


def oh_my_page(request):
    context = {

    }
    return render(request, 'Toolshop/ohMy.html', context)





'''

def blog_home(request):
    recent_blog_list = Blog.objects.order_by('-posted')[:3]
    context = {
        'recent_blog_list': recent_blog_list,
    }
    return render(request, 'blog/index.html', context)


def blog_archive(request):
    blog_list = Blog.objects.order_by('-posted')
    context = {
        'recent_blog_list': blog_list,
    }
    return render(request, 'blog/archive.html', context)


def blog_entry(request, blog_id):
    blog_obj = get_object_or_404(Blog, pk=blog_id)
    comments_list = blog_obj.comments_set.all().order_by('-posted')

    context = {
        'blog': blog_obj,
        'comments_list': comments_list,
        'blog_id': blog_id,
    }
    return render(request, 'blog/entry.html', context)


def about(request):
    return render(request, 'blog/about.html', {'Server_Time': timezone.now()})

'''

