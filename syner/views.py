from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'syner/home.html')

def signin(request):
    return render(request, 'syner/signin.html')

def signup(request):
    return render(request, 'syner/signup.html')

def dashboard(request):
    return render (request, 'syner/dashboard.html')