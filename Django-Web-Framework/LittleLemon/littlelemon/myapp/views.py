from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu


# Create your views here.
def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")

def book(request):
    return HttpResponse("Booking")

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request, 'menu.html', main_data)