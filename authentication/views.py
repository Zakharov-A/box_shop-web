from django.shortcuts import render

# Create your views here.

def login_user(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')


def logout_user(request):
    pass


