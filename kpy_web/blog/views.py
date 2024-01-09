from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CommentForm

def list(req):
    Data = {'Posts': Post.objects.all().order_by("-created_at")}
    return render(req, 'blog/blog.html', Data)
def post(req, id):
    post = get_object_or_404(Post, pk=id)
    comments = post.comments.all()
    return render(req, 'blog/post.html', {'post': post, 'comments': comments})
def add_comment(req, id):
    post = get_object_or_404(Post, pk=id)
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = req.user
            comment.save()
            return redirect('post',id=id)
    else:
        form = CommentForm()
    return render(req, 'blog/post.html', {'form': form, 'post': post}) 