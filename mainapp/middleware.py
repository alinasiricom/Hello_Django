from django.shortcuts import reverse, redirect
from django.conf import settings


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get('PATH_INFO', "")

        if settings.MAINTENANCE_MODE and path!= reverse("mainapp:maintenance"):
            response = redirect(reverse("mainapp:maintenance"))
            return response

        response = self.get_response(request)

        return response