from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListAPIView

# creating an api view
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer