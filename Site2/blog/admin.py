from django.contrib import admin
from blog.models import Post, Category, Message, ChatRoom

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(ChatRoom)