from django.contrib import admin
from .models import Logger, Reservation, Employees

# Register your models here.
# admin.site.register(Drinks)
# admin.site.register(Menu)
# admin.site.register(MenuCategory)
# admin.site.register(Drinks)
# admin.site.register(DrinksCategory)
# admin.site.register(Logger)

admin.site.register(Reservation)
admin.site.register(Employees)