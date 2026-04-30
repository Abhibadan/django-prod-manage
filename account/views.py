from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect("admin")
                else:
                    role = user.groups.first().name
                    request.session["role"] = role
                    print(request.session.get("role"))
                    messages.success(request, "Login successfully")
                    return redirect("dashboard")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_active = True

            user.set_password(form.cleaned_data["password"])
            user.save()
            user.groups.add(form.cleaned_data["role"])
            auth_login(request, user)
            role = user.groups.first().name
            request.session["role"] = role
            messages.success(request, "Registered successfully")
            return redirect("dashboard")
    else:
        form = UserRegistrationForm()
        
    return render(request, "register.html", {"form": form})

def logout(request):
    auth_logout(request)
    return redirect("login")
