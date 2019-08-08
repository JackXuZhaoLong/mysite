from django.urls import  path
from . import views

#http://localhost:8000/blog
urlpatterns =[
    path('',views.blog_list, name='blog_list'),
    path('<blog_pk>',views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>',views.blog_with_type, name='blog_with_type'),
]
