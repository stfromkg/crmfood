from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from crmfood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crmfood.urls'))
]
