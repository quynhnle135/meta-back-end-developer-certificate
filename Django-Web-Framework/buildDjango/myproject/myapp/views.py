from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm

def home(request):
    return HttpResponse('Welcome to Little Lemon!')

def about(request):
    return HttpResponse('About us')

def book(request):
    return HttpResponse('Make a booking')

def menu(request):
    return HttpResponse('Menu for Little Lemon')

def form_view(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'home.html', context)

def drinks(request, drink_name):
    drinks = {
        'mocha': 'type of coffee',
        'tea': 'type pf beverage',
        'lemonade': 'type of refreshment'
    }

    choice_of_drink = drinks[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)