from django.urls import path
from .views import register, login_user, logout_user, home, posts

# app-name = "blog"

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('posts/', posts, name='posts')
]