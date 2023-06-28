from django.db import models


# class Menuitems(models.Model):
#     itemname = models.CharField(max_length=200)
#     category = models.CharField(max_length=300)
#     year = models.IntegerField()

# class Drinks(models.Model):
#     drink_name = models.CharField(max_length=200)
#     price = models.IntegerField()

# class MenuCategory(models.Model):
#     menu_category_name = models.CharField(max_length=200)


# class Menu(models.Model):
#     menu_item = models.CharField(max_length=200)
#     price = models.IntegerField(null=False)
#     category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)

# class DrinksCategory(models.Model):
#     category_name = models.CharField(max_length=200)
    
# class Drinks(models.Model):
#     drink = models.CharField(max_length=200)
#     price = models.IntegerField()
#     category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")


class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self) -> str:
        return self.name


class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name