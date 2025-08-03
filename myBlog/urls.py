from django.urls import path 
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',post_list_view,name='post_list'),
    path('post/<int:pk>/',post_detail_view,name='post_detail'),
    path('post/new/',post_add_view,name='post_add'),
    path('post/<int:pk>/update/',post_update_view,name='post_update'),
    path('post/<int:pk>/delete/',post_delete_view,name='post_delete'),
]
