from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')

def teams(request):
    # Matthew's part
    pass

def tasks(request):
    return render(request, 'tasks-admin.html')

def tasks_employee(request): 
    return render(request, 'tasks-employee.html')
    # This is a temporary function to load tasks-employee.html, when working on the backend of the project, we can make an "if" statement in previous function that says if user.permission_level == 1, display tasks-employees.html else if user.permission_level == 8 or 9, then display tasks-admin.html

    
