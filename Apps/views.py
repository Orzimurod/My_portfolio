from django.shortcuts import render

from .models import Education, PortfolioItem, Post, Experience


def home_view(request):
    items = PortfolioItem.objects.all()
    education = Education.objects.all()
    post = Post.objects.all()
    experience = Experience.objects.all()
    form = {
        'items': items,
        'education': education,
        'post': post,
        'experience': experience,
    }
    return render(request, 'index.html', form,)


def posts_list(request):
    post_all = Post.objects.all()
    return render(request, 'post_detail.html', {'post_all': post_all})
