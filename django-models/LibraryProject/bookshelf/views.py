from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def hello_view(request):
    """Function-based view for the hello/ URL."""
    return HttpResponse('Hello, Django!')