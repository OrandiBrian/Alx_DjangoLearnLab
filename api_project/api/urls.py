from .views import BookListAPIView
from django.urls import path

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list')
]