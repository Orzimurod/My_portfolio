from django.shortcuts import render

from .models import Education, PortfolioItem,Post

def home_view(request):
    items = PortfolioItem.objects.all()
    education = Education.objects.all()
    post = Post.objects.all()
    form = {
        'items': items,
        'education': education,
        'post': post,
    }
    return render(request,'index.html',form,)





