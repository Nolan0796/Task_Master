from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')
