from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'syner/home.html')

def signin(request):
    return render(request, 'syner/Signin.html')

def signup(request):
    return render(request, 'syner/Signup.html')

def dashboard(request):
    return render (request, 'syner/dashboard.html')