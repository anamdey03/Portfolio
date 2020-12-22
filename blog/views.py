from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/allblogs.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)
