from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # processamento antes de mostrar a home page
    return render(request, 'MeuApp/home.html')

def segundaPagina(request):
    # processamento antes de mostrar a segunda página
    return render(request, 'MeuApp/segunda.html')
