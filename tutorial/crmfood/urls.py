from django.urls import path
from crmfood import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('roles', views.RolesView.as_view()),
    path('users', views.UsersView.as_view()),
    path('checks', views.ChecksView.as_view()),
    path('meals', views.MealsView.as_view()),
    path('meals_meal_by_category', views.Meals_meal_by_categoryView.as_view()),
    path('meal_categories_for_Dep', views.Meal_categories_for_DepView.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('meal_to_order', views.Meal_to_OrderView.as_view()),
    path('meal_categories', views.Meal_Categories.as_view()),
    path('departments', views.Departments.as_view()),
    path('active_orders', views.Active_orders.as_view()),
    path('tables', views.Tables.as_view()),
    path('statuses', views.Statuses.as_view()),
    path('service_persentage', views.Service_Persentage.as_view()),
    path('orders/<int:pk>', views.OrderDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)