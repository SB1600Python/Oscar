from django import forms
from blog.models import Post, Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'category')

class ChatForm(forms.ModelForm):
    module = Message
    fields = ('author','text')
