from django.shortcuts import render


def index(request):
    return render(request, 'main_pages/main_page.html')


def about(request):
    return render(request, 'main_pages/about_page.html')


def chess(request):
    return render(request, 'main_pages/chess.html')
