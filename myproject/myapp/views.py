from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .models import Member

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        details = InputForm(request.POST)
        member = Member()
        member.first_name =  details['user_name'].value()
        member.pw = details['password'].value()
        for obj in Member.objects.all():
            print(obj.first_name)
        member.save()
        print(details['user_name'].value())

    context={}
    context['form']=InputForm()
    return render(request, 'login.html', context)

def blog(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def blog5(request):
    return render(request, 'blog5.html')

def blog10(request):
    return render(request, 'blog10.html')