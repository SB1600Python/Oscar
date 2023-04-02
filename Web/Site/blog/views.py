from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'ab  out.html', {})


def register(request):
    return render(request, 'register.html', {})


def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'detail.html', {"post": post})

