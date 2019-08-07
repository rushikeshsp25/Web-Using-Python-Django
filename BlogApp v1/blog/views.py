from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from .models import Author,Post
# Create your views here.
def feed(request):
    posts_qs = Post.objects.all()
    posts_li = []
    for post in posts_qs:
        posts_li.append({
            'title':post.title,
            'content':post.content
        })
    return JsonResponse({'posts':posts_li})

def year_archive(request,year):
    posts_qs = Post.objects.filter(date_posted__year = year)
    posts_li = []
    for post in posts_qs:
        posts_li.append({
            'title':post.title,
            'content':post.content
        })
    return JsonResponse({'year':year,'posts':posts_li})

def month_archive(request,year,month):
    posts_qs = Post.objects.filter(date_posted__year=year, date_posted__month=month)
    posts_li = []
    for post in posts_qs:
        posts_li.append({
            'title':post.title,
            'content':post.content
        })
    return JsonResponse({'year':year,'month':month,'posts':posts_li})

def post_detail(request,year,month,pk):
    posts_qs = Post.objects.filter(date_posted__year=year, date_posted__month=month,id = pk)
    posts_li = []
    for post in posts_qs:
        posts_li.append({
            'title':post.title,
            'content':post.content
        })
    return JsonResponse({'year':year,'month':month,'pk':pk,'posts':posts_li})