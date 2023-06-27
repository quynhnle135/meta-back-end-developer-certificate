from django.contrib import admin
from .models import Menu, MenuCategory, Drinks, DrinksCategory

# Register your models here.
# admin.site.register(Drinks)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
