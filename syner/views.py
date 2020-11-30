from django.shortcuts import render
from .forms import SignupForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    return render(request, 'syner/home.html')

def signin(request):
    return render(request, 'syner/Signin.html')

@csrf_protect
def signup(request):

    form = SignupForm()


    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' :form}
    return render(request, 'syner/Signup.html', context)

def dashboard(request):
    return render (request, 'syner/dashboard.html')