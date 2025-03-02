from django.urls import path
from django.urls import path
from .views import list_books, LibraryDetailView, register_user, login_user
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from .views import admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', member_view, name='member_dashboard'),
    path("add/", add_book, name="add_book"),
    path("edit/<int:book_id>/", edit_book, name="edit_book"),
    path("delete/<int:book_id>/", delete_book, name="delete_book"),
]