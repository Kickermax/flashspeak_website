from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing_page.html')


def cards(request):
    return render(request, 'cards.html')
