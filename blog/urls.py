#!/usr/bin/env python

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns =[
    path('',views.index,name='index'),
    path('posts/<int:pk>/',views.detail,name='detail'),
#        归档页面
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
#    分类页面
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    ]
