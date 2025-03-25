from .views import BookList, BookViewSet, UserView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# defining routers
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# defining urls
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('token/', UserView.as_view(), name='token')
]