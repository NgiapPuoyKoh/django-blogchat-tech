from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('posts/', views.all_posts, name='posts'),
    # path('<post_id>', views.post_detail, name='post_detail')
    path('<slug:post>/', views.post_detail, name='post_detail')
]
