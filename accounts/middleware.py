# # accounts/middleware.py

# from django.conf import settings
# from django.shortcuts import redirect
# from django.urls import reverse

# class RedirectIfAuthenticatedMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             if request.path in [reverse('login'), reverse('register'), reverse('dashboard')]:
#                 return redirect(settings.LOGIN_REDIRECT_URL)  # Redirect to home page or dashboard
#         response = self.get_response(request)
#         return response
