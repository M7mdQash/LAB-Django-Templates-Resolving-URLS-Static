from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request):
    return render(request, 'mainApp/home.html')


def terms_view(request):
    return render(request, 'mainApp/terms.html')
