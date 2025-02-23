from django.urls import path
from django.urls import path
from .views import list_books, LibraryDetailView, register_user, login_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]