from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def role_required(role):
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.UserProfile.role == role:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapped
    return decorator