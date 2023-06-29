from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import LogForm

def home(request):
    return HttpResponse('Welcome to Little Lemon!')

def about(request):
    # return HttpResponse('About us')
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", about_content)

def menu(request):
    menu_content = {'menu': 'Little Lemon menu'}
    return render(request, "menu.html", menu_content)

def book(request):
    return HttpResponse('Make a booking')

# def menu(request):
#     return HttpResponse('Menu for Little Lemon')

def form_view(request):
    form =  LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
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