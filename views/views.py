from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>v 1.6.000</h1>")