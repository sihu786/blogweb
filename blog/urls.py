
from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('blogs/',blog,name='blog'),
    path('category_blogs/<str:slug>/',category_blogs,name='category_blogs'),
    path('tags_blogs/<str:slug>/',tag_blogs,name='tags_blogs'),
    path('blog_details/<str:slug>/',blog_details,name='blog_details'),
    path('search_blogs/',search_blog,name='search_blogs'),
    path('contact/',contact,name='contact_url'),
   
    
]
