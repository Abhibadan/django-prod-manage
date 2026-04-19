from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "admin":
            return redirect("product_list")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})
    