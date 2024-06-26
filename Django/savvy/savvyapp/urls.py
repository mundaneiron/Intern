from django.urls import path
from . import views
from .views import get_posts, create_post, signin

urlpatterns = [
    path('', views.index, name='homePage'),
    path('home/', views.home, name='home'),
    path('signin/', signin, name='signin'),
    path('insert/', views.insert, name='insert'),
    path('api/posts/', get_posts, name='get_posts'),
    path('api/posts/create/', create_post, name='create_post'),
]
