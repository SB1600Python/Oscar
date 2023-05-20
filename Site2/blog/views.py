from django.shortcuts import render, redirect,HttpResponseRedirect, get_object_or_404
from blog.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from blog.forms import PostForm, ChatForm 

def view_login(request):
     if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username, password=password)
               if user is not None:
                    login(request, user)
                    return redirect('home')
     else:
          form = AuthenticationForm()
     return render(request, 'login.html', {'form': form})


# Create your views here.
def index(request):
     posts = Post.objects.all()
     paginator = Paginator(posts, 3)
     page = request.GET.get('page')
     try:
          posts = paginator.page(page)
     except PageNotAnInteger:
          posts = paginator.page(1)
     except EmptyPage:
          posts = paginator.page(paginator.num_pages)
     return render(request, 'index.html', {"page": page, "posts": posts})

def detail(request, pk):
     post = Post.objects.get(id=pk)
     return render(request, 'detail.html', {"post": post})

class RegisterView(View):
     form_class = UserCreationForm
     temlate_name = 'register.html'

     def get(self, request):
          form = self.form_class()
          return render(request, self.temlate_name, {'form': self.form_class})

     def post(self, request):
          form = self.form_class(request.POST)
          if form.is_valid():
               user = form.save()
               return redirect('login')
          return render(request, self.temlate_name, {'form': form})


def logout_view(request):
     logout(request)
     return redirect('login')

def create_post(request):
     return redirect('home')


class PostView(LoginRequiredMixin, CreateView):
     model = Post
     template_name = 'create.html'
     form_class = PostForm


def delete(request, id):
     try:
          post = Post.objects.get(id=id)
          post.delete()
          return redirect('home')
     except:
          return HttpResponseRedirect('/')
     
          

          
def update(request, id):
     try:
          post = get_object_or_404(Post, id)

          if request.method == 'GET':
               form = PostForm(instance=post)
               if request.user is not post.authot:
                    return render(request, 'update.html', {'form' : form})
               
          if request.method == 'POST':
               form = PostForm(request.POST, isinstance=post )
               if form.is_vaild():
                    form.save
                    return redirect('home')

     except Exception as e:
          print(e)
          return HttpResponseRedirect('/')


def chat(request, room_id):
     room = ChatRoom.objects.get(id=room_id)
     messages = room.massages.all()

     if request.method == 'GET':
          message_text= request.POST.get('message')
          message_user = request.user
          message = Message.objects.create(room=room, text=message_text, author=message_user )
          messages = room.massages.all()
     return render(request, 'chat.html', {'room': room, 'messages': messages})

