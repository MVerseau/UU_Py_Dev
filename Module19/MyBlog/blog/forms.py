from django import forms
from .models import Post



class PostsPerPage(forms.Form):
    choices = (
        ('3', 'по 3 поста'),
        ('5', "по 5 постов"),
        (str(len(Post.objects.all())), "Все посты"),

    )
    number = forms.ChoiceField(choices=choices, widget=forms.Select(), required=False, label='На странице')


