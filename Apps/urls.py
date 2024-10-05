from django.urls import path

from Apps.views import home_view, posts_list


urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', posts_list, name='post_list'),
]
