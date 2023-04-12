from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

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

class UserListView(ListView):
    model = User
    template_name = 'registration/index.html'

def register_user(request):
        if request.method == "GET":
            return render(
                request, "registration/create.html",
                {"form": CustomUserCreationForm}
            )
        elif request.method == "POST":
            form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("User created successfully"))
            return redirect('users-index')
        else:
            messages.success(request, ("Something went wrong please try again"))
            return redirect('register-user')
        

class UserUpdateView(UpdateView):
    model = User
    template_name = 'registration/update.html'
    form_class = CustomUserCreationForm
    success_message = "User updated successfully"
    
    def get_success_url(self):
        return reverse("users-index")

class UserDeleteView(DeleteView):
    model = User
    success_message = "User deleted successfully"
    
    def get_success_url(self):
        return reverse("users-index")
