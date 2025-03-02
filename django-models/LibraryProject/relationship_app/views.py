from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


# Function based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# class based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add library books to the context
        context['books'] = self.objects.books.all()
        return context

# register user   
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# login user 
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')  # Redirect to your books page after login
    return render(request, 'relationship_app/login.html')

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# # User roles
# @role_required('ADMIN')
# def admin_view(request):
#     return render(request, 'admin_dashboard.html', {
#         'title': 'Admin Dashboard',
#         'message': 'Welcome to the Admin Dashboard'
#     })

# @role_required('LIBRARIAN')
# def librarian_view(request):
#     return render(request, 'librarian_dashboard.html', {
#         'title': 'Librarian Dashboard',
#         'message': 'Welcome to the Librarian Dashboard'
#     })

# @role_required('MEMBER')
# def member_view(request):
#     return render(request, 'member_dashboard.html', {
#         'title': 'Member Dashboard',
#         'message': 'Welcome to the Member Dashboard'
#     })