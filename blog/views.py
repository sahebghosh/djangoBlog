from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blogs
from . import forms


def blog_list(request):
    queryset = Blogs.objects.all().order_by('date')
    context = {
        'blogList': queryset
    }
    return render(request, 'blog/bloglist.html', context)

@login_required(login_url='userAccount:login')
def create_blog(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Successfully, you have created new blog.....')
            return redirect('blog:list')
    else:
        form = forms.CreateBlog()

    context = {
        'form': form
    }
    return render(request, 'blog/createblog.html', context)

def blog_detail(request, slug):
    queryset = Blogs.objects.get(slug = slug)
    context = {
        'blog': queryset
    }
    return render(request, 'blog/blogdetail.html', context)
