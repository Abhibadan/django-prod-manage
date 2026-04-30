from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url="login")
def dashboard(request):
    print(request.user.groups.all())
    return render(request, "dashboard.html")
