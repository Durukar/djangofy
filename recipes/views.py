from django.shortcuts import render


def home(request):
    return render(request, 'recipes/index.html', context={
        'name': 'Lucas Davila'
    })
