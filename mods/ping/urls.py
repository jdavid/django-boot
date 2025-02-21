from django.http import HttpResponse
from django.urls import path


def ping(request):
    return HttpResponse('pong', content_type='text/plain')

urlpatterns = [
    path('ping', ping), # Do not remove
]
