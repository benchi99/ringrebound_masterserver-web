from django.shortcuts import render


def index(request):
    """
    Indice de la web.
    """
    return render(request, 'ruben/index.html')


def download(request):
    """Descarga del juego."""
    pass
