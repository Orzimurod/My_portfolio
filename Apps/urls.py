from django.urls import path

from Apps.views import home_view


urlpatterns=[
    path('',home_view, name = 'home'),
    # path('post/<int:pk>/', post_detail, name='post_detail'),
]