from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='mennu'),
    path('book/', views.book, name='book'),
    path('form/', views.form_view, name="form"),
    path('drinks/<str:drink_name>', views.drinks),
]