from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/index.html', context={
        'name': 'Lucas Davila'
    })


def sobre(request):
    return render(request, 'recipes/sobre.html')
    # return HTTP Response


def contato(request):
    return HttpResponse('Sobre')
    # return HTTP Response
