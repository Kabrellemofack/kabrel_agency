from django.shortcuts import render, redirect
from .models import Register
from django.contrib import messages

# Vue pour la page d'accueil
def home(request):
    return render(request, 'home.html')

# Vue pour la page de connexion
def login(request):
    return render(request, 'login.html')

# Vue pour la page d'inscription
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prename = request.POST.get('prename')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'register.html')

        # Vérifie si l'email existe déjà
        if Register.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, 'register.html')

        # Enregistre l'utilisateur
        Register.objects.create(name=name, prename=prename, email=email, password=password)
        messages.success(request, "Compte créé avec succès !")
        return redirect('home')  # Redirige vers la page d'accueil après l'inscription

    return render(request, 'register.html')

# Vue pour la page de l'hôtel
def hotel(request):
    return render(request, 'hotel.html')