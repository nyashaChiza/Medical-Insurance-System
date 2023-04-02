from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.forms import UserCreationForm


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f"You have successfully logged in as: {user.username}"))
            return redirect('dashboard')
        
        else:
            messages.success(request, ("Please check your credentials and try again"))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
