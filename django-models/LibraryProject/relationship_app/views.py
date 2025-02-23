from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

# Function based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# class based view
class library_detail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add library books to the context
        context['books'] = self.objects.books.all()
        return context