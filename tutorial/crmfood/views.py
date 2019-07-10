from crmfood.models import *
from crmfood.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from  rest_framework.views import APIView
class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class UsersView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ChecksView(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer


class MealsView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class Meals_meal_by_categoryView(generics.ListCreateAPIView):
    queryset = Meals_meal_by_category.objects.all()
    serializer_class = Meals_meal_by_categorySerializer


class Meal_categories_for_DepView(generics.ListCreateAPIView):
    queryset = Meal_categories_for_Dep.objects.all()
    serializer_class = Meal_categories_for_DepSerializer


class OrdersView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    def get(self, request):
        return Response('hello/n you cannot see!')


class Meal_to_OrderView(generics.ListCreateAPIView):
    queryset = Meal_to_Order.objects.all()
    serializer_class = Meal_to_OrderSerializer


class Meal_Categories(generics.ListCreateAPIView):
    queryset = Meal_Categories.objects.all()
    serializer_class = Meal_CategoriesSerializer


class Departments(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class Active_orders(generics.ListCreateAPIView):
    queryset = Active_orders.objects.all()
    serializer_class = Active_ordersSerializer

class OrderDetail(APIView):
    def get_object(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request,  pk, format= None):
        snippet = self.get_object(pk)
        serializer = OrdersSerializer(snippet)
        return Response(serializer.data)

class Tables(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class Statuses(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class Service_Persentage(generics.ListCreateAPIView):
    queryset = Service_Persentage.objects.all()
    serializer_class = Service_PersentageSerializer
