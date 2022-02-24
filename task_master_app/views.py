from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):

    return render(request, 'register.html')
