from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def lists(request):
    post = Post.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'lists.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post
    }
    return render(request, 'detail.html', context)

def create(request):
    title = request.POST['title']
    content = request.POST['content']
    post = Post(title=title, content=content, created_at=timezone.now())
    post.save()
    return redirect('post:detail', post_id=post.id)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post
    }
    return render(request, 'edit.html', context)

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.post_active = True
    post.save()
    return redirect('post:detail', post_id=post.id)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post:lists')
