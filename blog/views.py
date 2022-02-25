from http.client import HTTPResponse
from django.shortcuts import redirect, render
from blog.forms import CommentForm, PostForm
from .models import Post

def frontpage(request):
    if request.method == "POST":
        form =PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request,"blog/frontpage.html", {'posts':posts ,'form': form})

def post_detail(request, slug):
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


