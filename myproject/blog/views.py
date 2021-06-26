from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)


def update(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.writer = request.POST["writer"]
        blog.body = request.POST["body"]
        blog.save()
        return redirect('detail', blog.id)
    return render(request, 'update.html', {"blog": blog})


def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("home")
