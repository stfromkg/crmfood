from crmfood.models import *
from crmfood.serializers import *
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import *
from django.http import Http404
from  rest_framework.views import APIView
from django.contrib.auth.models import User
from crmfood.serializers import UserSerializer
import re

def checkphone (phone):
    res = re.findall(r'\+996\d{9}', phone)
    if len(res)==1:
        return True
    else:
        return False


def checkdate(date):
    res1 = re.findall(r'\d{2}:\d{2}:\d{4}', date)
    res2 = re.findall(r'\d{2}-\d{2}-\d{4}', date)
    res3 = re.findall(r'\d{2}\.\d{2}\.\d{4}', date)
    res4 = re.findall(r'\d{2}/\d{2}/\d {4}', date)

    if len(res1)==1 or len(res2)==1 or len(res3)==1 or len(res4)==1:
        return True
    else:
        return False



class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    def get(self, request):
        return Response('hello/n you cannot see roles view!')

class RolesDetail(generics.RetrieveAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def post(self, request):
        phone = request.data['phone']
        data = request.data['dateofadd']

        if checkphone(phone) and checkdate(date):
            serializer = UsersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data)

        else:
            return Response('Error')
    # def get(self, request):
    #     return Response('hello/n you cannot see users view!')


    def post(self, request):
        print('Function def post was ready')
        return Response()

class UsersDetail(APIView):
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request,  pk, format= None):
        snippet = self.get_object(pk)
        serializer = UsersSerializer(snippet)
        return Response(serializer.data)


class ChecksView(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer
    def get(self, request):
        return Response('hello/n you cannot see checks view!')

class ChecksDetail(APIView):
    def get_object(self, pk):
        try:
            return Checks.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request,  pk, format= None):
        snippet = self.get_object(pk)
        serializer = ChecksSerializer(snippet)
        return Response(serializer.data)



class MealsView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request):
        return Response('hello/n you cannot see meals view!')

class MealsDetail(APIView):
    def get_object(self, pk):
        try:
            return Meals.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request,  pk, format= None):
        snippet = self.get_object(pk)
        serializer = MealsSerializer(snippet)
        return Response(serializer.data)



class Meals_meal_by_categoryView(generics.ListCreateAPIView):
    queryset = Meals_meal_by_category.objects.all()
    serializer_class = Meals_meal_by_categorySerializer
    def get(self, request):
        return Response('hello/n you cannot see meals meal by_category!')

class Meals_meal_by_categoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Meals_meal_by_category.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request,  pk, format= None):
        snippet = self.get_object(pk)
        serializer = Meals_meal_by_categorySerializer(snippet)
        return Response(serializer.data)



class Meal_categories_for_DepView(generics.ListCreateAPIView):
    queryset = Meal_categories_for_Dep.objects.all()
    serializer_class = Meal_categories_for_DepSerializer
    def get(self, request):
        return Response('hello/n you cannot see meal categories for_Dep!')

class Meal_categories_for_DepDetail(APIView):
    def get_object(self, pk):
        try:
            return Meal_categories_for_Dep.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request,  pk, format= None):
        snippet = self.get_object(pk)
        serializer = Meal_categories_for_DepSerializer(snippet)
        return Response(serializer.data)


class OrdersView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request):
        return Response('hello/n you cannot see orders view!')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OrdersDetail(generics.RetrieveAPIView):   #сделать так для всех Detail
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrdersGetView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersGetSerializer

class Meal_to_OrderView(generics.ListCreateAPIView):
    queryset = Meal_to_Order.objects.all()
    serializer_class = Meal_to_OrderSerializer
    def get(self, request):
        return Response('hello/n you cannot see meal to order view!')

class Meal_to_OrderDetail(generics.RetrieveAPIView):
    queryset = Meal_to_Order.objects.all()
    serializer_class = Meal_to_OrderSerializer


class Meal_Categories(generics.ListCreateAPIView):
    queryset = Meal_Categories.objects.all()
    serializer_class = Meal_CategoriesSerializer
    def get(self, pk):
        return Response('hello/n you cannot see orders meal categories!')

class Meal_CategoriesDetail(generics.RetrieveAPIView):
    queryset = Meal_Categories.objects.all()
    serializer_class = Meal_CategoriesSerializer


class Departments(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    def get(self, pk):
        return Response('hello/n you cannot see orders department!')

class DepartmentsDetail(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer



class Active_orders(generics.ListCreateAPIView):
    queryset = Active_orders.objects.all()
    serializer_class = Active_ordersSerializer

    def post(self, request):
        dat= request.data['date']
        a = re.findall(r'\d\d/\d\d/\d{4}', dat)
        if len(a)!=1:
            return Response('ваша дата не корректна')
        else:
            serializer = Active_ordersSerializer(data=request.data)
            if serializer.is_valid():
                a = request.data

     # def get(self,  pk):
     #   return Response('hello/n you cannot see orders active orders!')
     #            return Response(a)

class Active_ordersDetail(generics.RetrieveAPIView):
    queryset = Active_orders.objects.all()
    serializer_class = Active_ordersSerializer





class Tables(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    def get(self, pk):
        return Response('hello/n you cannot see tables!')

class TablesDetail(generics.RetrieveAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class Statuses(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer
    def get(self, pk):
        return Response('hello/n you cannot see statuses!')

class StatusesDetail(generics.RetrieveAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer

class Service_PersentageView(generics.ListCreateAPIView):
    queryset = Service_Persentage.objects.all()
    serializer_class = Service_PersentageSerializer

    def post(self, request):
        res= request.data['persentage']
        if int(res) <= 0:
            return Response('ваше число отрицательное')
        else:
            serializer = Service_PersentageSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
            return Response("ваше число положительное ")
    def get(self, request, pk):
        return Response('hello/n you cannot see service persentage!')


class Service_PersentageDetail(generics.RetrieveAPIView):
    queryset = Service_Persentage.objects.all()
    serializer_class = Service_PersentageSerializer