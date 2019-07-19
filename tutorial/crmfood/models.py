from django.db import models
import re
# Create your models here.

class Statuses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Service_Persentage(models.Model):
    persentage = models.IntegerField(default=True)

    def __str__(self):
        return self.persentage


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    dateofadd = models.CharField(max_length=20)
    roleid= models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, related_name='users', default=True)
    def __str__(self):
        return self.name



class Departments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Meal_Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='deps', default=True)
    def __str__(self):
        return self.name

class Meal_to_Order(models.Model):
    uniqueid = models.IntegerField(default=True)
    orderid = models.IntegerField(default=True)
    meals =models.ForeignKey(Meal_Categories, on_delete=models.CASCADE, related_name='meal_to_order', default=True)
    def __str__(self):
        return self.meals.name


class Orders(models.Model):

    waiterid = models.IntegerField(default=True)
    tableid = models.IntegerField(default=True)
    tablename = models.CharField(max_length=50)
    isitopen = models.IntegerField(default=True)
    date = models.IntegerField(default=True)
    mealsid = models.ManyToManyField(Meal_Categories, related_name="meal_categories", default=True)
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return str(self.date)

class Meal_categories_for_Dep(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='mcfd', default=True)
    def __str__(self):
        return self.name

class Meals_meal_by_category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Meal_categories_for_Dep, on_delete=models.SET_NULL, null=True, related_name='meals_meal_by_category', default=True)
    price = models.IntegerField(default=True)
    decription = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Meals(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Meals_meal_by_category, on_delete=models.SET_NULL, null=True, related_name='meals', default=True)  #
    price = models.IntegerField(default=True)
    decription = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Checks(models.Model):
    id = models.IntegerField(primary_key=True)
    orderid = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='checks', default=True)
    date = models.IntegerField(default=True)
    servicefee = models.IntegerField(default=True)
    totalsum = models.IntegerField(default=True)
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='checks', default=True)
    def __str__(self):
        return self.name



class Tables(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Active_orders(models.Model):
    id = models.IntegerField(primary_key=True)
    waiterid = models.IntegerField(default=True)
    tablename = models.ForeignKey(Tables, on_delete=models.CASCADE, related_name='active_orders', default=True)
    isitopen = models.IntegerField(default=True)
    date = models.CharField(max_length=50)
    mealsid = models.IntegerField(default=True)
    def __str__(self):
        return self.name




