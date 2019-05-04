from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('createblog/', views.create_blog, name='create'),
    path('<slug>/', views.blog_detail, name='detail'),
]
