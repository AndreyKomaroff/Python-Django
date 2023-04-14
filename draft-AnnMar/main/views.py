from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html', {'title': 'Главная!', 'h1': 'Hello'})

def blog(request):
    return render(request, 'main/blog.html', {'title': 'Блог', 'h1': 'Блог'})

def portfolio(request):
    return render(request, 'main/portfolio.html', {'title': 'Портфолио', 'h1': 'Портфолио'})
