from rest_framework import serializers
from crmfood.models import *
from django.contrib.auth.models import User


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ('name',)

class UserSerializer(serializers.ModelSerializer):

    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())


    class Meta:
        model = User
        fields = ('id','username', 'orders', )


class UsersSerializer(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields = ('name','surname','login','password', 'email', 'phone', 'dateofadd','roleid', )



class ChecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checks
        fields = ('orderid', 'date', 'servicefee', 'totalsum','meals', )


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ('name','categoryid', 'price', 'decription', )


class Meals_meal_by_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals_meal_by_category
        fields = ('name','categoryid', 'price', 'decription', )


class Meal_categories_for_DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_categories_for_Dep
        fields = ('name', 'department',)


class Meal_CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_Categories
        fields = ('name','department',   )

class OrdermiddleSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model= Meal_Categories
        fields = ('name',)

class OrdersSerializer(serializers.ModelSerializer):
    mealsid = OrdermiddleSerializer(many=True, queryset=Meal_Categories.objects.all())
    class Meta:
        model = Orders
        fields = ('waiterid', 'tablename', 'isitopen', 'date','mealsid',   )

    def create(self, validated_data):
        print(validated_data)
        res=validated_data.pop('mealsid')
        ordertmp = Orders.objects.create(**validated_data)
        a= Orders(**validated_data)
        a.save()
        for i in res:
            a.mealsid.add(i)
            a.save()
        return a

class OrdersGetSerializer(serializers.HyperlinkedModelSerializer):
    mealsid = Meal_CategoriesSerializer(many=True, read_only=True)
    class Meta:
        model = Orders
        fields = ('waiterid', 'tablename', 'isitopen', 'date','mealsid',   )

class Meal_to_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_to_Order
        fields = ('orderid', 'meals',  )





class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('name',  )


class Active_ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active_orders
        fields = ('waiterid','tablename','isitopen','date','mealsid',   )


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ('name',  )


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('name',  )


class Service_PersentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Persentage
        fields = ('persentage',  )


