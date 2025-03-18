from django.urls import path
from django.urls import path
from .views import list_books, LibraryDetailView, register_user, login_user, logout_user
from .views import admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("delete/<int:book_id>/", delete_book, name="delete_book"),
]