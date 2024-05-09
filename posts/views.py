from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *

# Create your views here.

def CreatePostView(request):
    if request.method == 'POST':
        user = request.user
        body = request.POST['body']
        if body != '':
            post = Post.objects.create(
                body=body,
                user=user
            )
            post.save()
            return redirect('posts:posts_list')
        return render(request, 'posts/posts_create.html')
    else:
        return render(
            request,
            'posts/posts_create.html'
        )

class PostListView(ListView):

    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'


def PostDetailsComment(request,id):
    comments = Comment.objects.all()
    if request.method == 'POST':
        user = request.user
        body = request.POST['body']
        post = Post.objects.get(id=id)
        if body != '':
            comment = Comment.objects.create(
                body=body,
                user=user,
                post=post
            )
            comment.save()
            return render(request,'posts/post_details.html',{'post':post,'comments':comments})
        return render(request,'posts/post_details.html',{'post':post})
    else:
        post = Post.objects.get(id=id)
        return render(request,'posts/post_details.html',{'post':post, 'comments':comments})
