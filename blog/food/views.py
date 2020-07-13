from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'Adams',
        'title': 'Recipe Post',
        'content': 'First post content',
        'date_posted': 'July 09, 2020',
    },

    {
        'author': 'Jian Yang',
        'title': '8 Octopus Recipes',
        'content': 'I hate Eric Bacman',
        'date_posted': 'July 09, 2020',
    },

{
        'author': 'User Name',
        'title': 'Post Title',
        'content': 'Short Description',
        'date_posted': 'July 09, 2020',
    }
]


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Testing title'
    }
    return render(request, 'food/home.html', context)

def about(request):
    return render(request, 'food/about.html', {'title': 'Django Food Blog'})
