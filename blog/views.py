from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'C',
        'title':'Blog post 1',
        'content':'First post',
        'date_posted':'xxx'
    },
    {
        'author':'C',
        'title':'Blog post 2',
        'content':'Second post',
        'date_posted':'xxx'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
      
