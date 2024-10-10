from django.shortcuts import redirect
from django.urls import reverse

class DisableChangePasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path == reverse('admin:password_change'):
            return redirect('/admin/')

        return response
