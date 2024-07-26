from django.shortcuts import get_object_or_404, render
from .models import Post
# from django.http import Http404


def post_list(request):
    posts = Post.published.all()
    return render(request,    'MyBlog/post/list.html',    {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'MyBlog/post/detail.html',
        {'post': post}
        )