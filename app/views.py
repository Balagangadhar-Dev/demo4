from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def products(request):
    return render(request, 'products.html')

def profile(request):
    return render(request, 'profile.html')

def orders(request):
    return render(request, 'orders.html')