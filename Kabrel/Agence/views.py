from django.shortcuts import render

# Create your views here.
#creation de la fonction home avec la pager home.html
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')