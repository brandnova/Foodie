# from django.conf import settings
# from django.shortcuts import redirect
# from django.urls import reverse

# def prevent_authenticated_access(view_func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             if request.path in [reverse('login'), reverse('register'), reverse('dashboard')]:
#                 return redirect(settings.LOGIN_REDIRECT_URL)  # Redirect to home page or dashboard
#         return view_func(request, *args, **kwargs)
#     return wrapper
