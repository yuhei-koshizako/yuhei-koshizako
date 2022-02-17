from http.client import HTTPResponse
from django.shortcuts import redirect, render

from blog.forms import CommentForm
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request,"blog/frontpage.html", {"posts": posts})

def post_deteil(request, slug):
    post = Post.objects.get(slug=slug)
    # print(f'request.method: {request.method}')
    if request.method == "POST":
        form = CommentForm(request.POST)
        #print(f'form: {form}')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})


