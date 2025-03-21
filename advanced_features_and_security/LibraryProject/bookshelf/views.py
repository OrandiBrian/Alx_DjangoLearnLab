from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """Function-based view for the book_list/ URL."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    """Function-based view for the create book/ URL."""
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        book = Book(title=title, author=author, publication_year=publication_year)
        book.save()
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    """Function-based view for the edit_book/ URL."""
    if request.method == 'POST':
        book = Book.objects.get(pk = book_id)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('book_list')
    else:
        book = Book.objects.get(pk = book_id)
        return render(request, 'edit_book.html', {'book': book})
    
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    """Function-based view for the delete_book/ URL."""
    book = Book.objects.get(pk = book_id)
    book.delete()
    return redirect('book_list')