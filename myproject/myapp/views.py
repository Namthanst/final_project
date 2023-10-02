from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def second(request):
    return render(request, 'login.html')

def blog(request):
    return render(request, 'blog1.html')