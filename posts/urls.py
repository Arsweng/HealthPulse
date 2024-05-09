from django.urls import path
from .views import *

urlpatterns = [
    path('',PostListView.as_view(),name='posts_list'),
    path('create/',CreatePostView, name='post_create'),
    path('<int:id>/',PostDetailsComment, name = 'comments')
]
app_name = 'posts'