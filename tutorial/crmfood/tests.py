from django.test import TestCase
from crmfood.models import Statuses, Orders
from django.contrib.auth.models import User
# Create your tests here.

class TestCase(TestCase):
    def setUp(self):
        testuser = User.objects.create(username='Melis',
                                       password = '123456')
        testuser = User.objects.get(username='Melis',
                                       password = '123456')
        Statuses.objects.create(name="new")
        Statuses.objects.create(name="close")
        Orders.objects.create(
            waiterid = 1,
            tableid = 1,
            tablename =1,
            isitopen = 1
            owner = testuser
        )
    def test_checkStatusCreate(self):
        var_one = Statuses.objects.get(name="close")
        var_two = Statuses.objects.get(name="new")
        self.assertEqual(var_one.name,"close" )
        self.assertEqual(var_two.name, "new")

    def test_checkOrdersCreate(self):
        order = Orders.objects.get(
            waiterid = 1,
            tableid = 1,
            tablename = 1,
            isitopen = 3,

        )
        self.assertEqual(order.isitopen, 1)