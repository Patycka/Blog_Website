from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='blog_index'),
    path('posts/', views.posts, name='blog_posts'),
    path('posts/<slug:slug>/', views.show_post, name='blog_single_post')
]