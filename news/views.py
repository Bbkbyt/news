from django.shortcuts import render
from news.models import *

# Create your views here.

def news_list(request):
    news=Post.objects.all()
    category=Category.objects.all()
    return render(request,'news/home.html',{'news':news,'category':category})