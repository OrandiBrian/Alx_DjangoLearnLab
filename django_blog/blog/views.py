from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# register user
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        
    else:
        form = UserCreationForm()
        
    return render(request, "blog/register.html", {"form": form})

# login view
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        
    else:
        form = AuthenticationForm(request)
    
    return render(request, 'blog/login.html')
        
        
# logout view
def logout_user(request):
    logout(request)
    return render(request, "blog/login.html")

# home view
def home(request):
    return render(request, "blog/home.html")

# post view
def posts(request):
    return render(request, "blog/blog_post.html")

# profile view
def profile(request):
    return render(request, "blog/profile.html")