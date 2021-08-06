from django.urls import path
# from .views import PostListViews
# from .views import PostDetailView
from .views import PostCreateView, PostUpdateView
# from .views import post_add
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('posts/', views.all_posts, name='posts'),
    # path('<post_id>/', views.post_detail, name='post_detail')
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('post/', PostDetailView.as_view(), name='post_detail')
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
]

#<app>/<model>_<viewtype>.html