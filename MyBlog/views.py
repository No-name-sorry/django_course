from django.shortcuts import get_object_or_404, render
from .models import Post
# from django.http import Http404


def post_list(request):
    posts = Post.published.all()
    return render(request,    'MyBlog/post/list.html',    {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'MyBlog/post/detail.html',
        {'post': post}
        )