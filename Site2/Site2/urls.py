"""Site2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import *

from django.conf import settings
from django.conf.urls.static import static

from weather import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('<int:pk>/', detail, name='detail'),
    path('login', view_login, name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', logout_view, name='logout'),
    # path('createPost', create_post, name='create'),
    path('create/', PostView.as_view(), name='create'),
    path('delete/<int:id>', delete, name= 'post_delete'),
    path('update/<int:id>', update, name= 'post_update'),
    path('chat/<int:room_id>',  chat, name= 'chat'),
    path('weather/', include('weather.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)