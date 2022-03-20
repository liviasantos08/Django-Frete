from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def tabela(request):
    return render(request, 'tables.html')
