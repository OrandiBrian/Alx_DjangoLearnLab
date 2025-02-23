from .models import Author, Book, Library, Librarian

# query all books by a specific author
author_name = Author.objects.get(name=author_name)
Book.objects.filter(author=author_name)

# list all books in a library
Library.objects.get(name=library_name).books.all()

# retrieve the librarian for a library
library = Library.objects.get(name='Main')
librarian = library.librarian