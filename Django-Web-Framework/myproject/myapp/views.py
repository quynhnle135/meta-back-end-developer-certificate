from django.shortcuts import render
from django.http import HttpResponse
from http.client import HTTPResponse

# def home(request):
#     return HttpResponse("<h1>Welcome to Little Lemon!</h1>")

# def home(request):
#     path = request.path
#     return HttpResponse(path, content_type='text/html', charset='utf-8')

# def home(request):
#     response = HttpResponse('This works!')
#     return response


# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     # provide header of object's path
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info

#     msg = f"""<br>
#             <br>Path: {path}
#             <br>Address: {address}
#             <br>Scheme: {scheme}
#             <br>Method: {method}
#             <br>User Agent: {user_agent}
#             <br>Path Info: {path_info}

#     """
#     return HttpResponse(msg, content_type='text/html', charset='utf-8')


# def drinks(request, drink_name):
#     drinks = {
#         'mocha': 'type of coffee',
#         'tea': 'type of beverage',
#         'lemonade': 'type of refreshment'
#     }
#     choice_of_drink = drinks[drink_name]
#     return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)

def home(request):
    return HttpResponse("Welcome to Little Lemon!")


def about(request):
    return HttpResponse("About us")


def menu(request):
    return HttpResponse("Menu")


def book(request):
    return HttpResponse("Make a booking")
