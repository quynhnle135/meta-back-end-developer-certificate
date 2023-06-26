from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Welcome to Little Lemon!</h1>")

# def home(request):
#     path = request.path
#     return HttpResponse(path, content_type='text/html', charset='utf-8')

# def home(request):
#     response = HttpResponse('This works!')
#     return response

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    # provide header of object's path
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    msg = f"""<br>
            <br>Path: {path}
            <br>Address: {address}
            <br>Scheme: {scheme}
            <br>Method: {method}
            <br>User Agent: {user_agent}
            <br>Path Info: {path_info} 

    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')