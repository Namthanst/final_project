from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
from django.contrib.auth.models import User
from .models import Member
from django.contrib import messages

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

def blog4(request):
    return render(request, 'blog4.html')

def blog6(request):
    return render(request, 'blog6.html')

def blog7(request):
    return render(request, 'blog7.html')

def blog8(request):
    return render(request, 'blog8.html')
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
def blog5(request):
    return render(request, 'blog5.html')

def blog9(request):
    return render(request, 'blog9.html')

def blog10(request):
    return render(request, 'blog10.html')

<<<<<<< Updated upstream
def cpmixlink(request):
    return render(request, 'cpmixlink.html')

def link(request):
    return render(request, 'blog3.html')    

def link1(request):
    return render(request, 'blog1.html')

def link2(request):
    return render(request, 'blog2.html')

def link4(request):
    return render(request, 'blog4.html')

def link5(request):
    return render(request, 'blog5.html')

def link6(request):
    return render(request, 'blog6.html')

def link7(request):
    return render(request, 'blog7.html')

def link8(request):
    return render(request, 'blog8.html')

def link9(request):
    return render(request, 'blog9.html')

def link10(request):
    return render(request, 'blog10.html') 

def review(request):
    return render(request, 'review.html') 

=======
>>>>>>> Stashed changes
