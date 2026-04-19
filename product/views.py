from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Product Management System")
    
def all_products(request):
    return HttpResponse("All Products")
