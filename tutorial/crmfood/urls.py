from django.urls import path
from crmfood import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('roles', views.RolesView.as_view()),
    path('users', views.UsersView.as_view()),
    path('checks', views.ChecksView.as_view()),
    path('meals', views.MealsView.as_view()),
    path('meals_meal_by_category', views.Meals_meal_by_categoryView.as_view()),
    path('meal_categories_for_dep', views.Meal_categories_for_DepView.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('meal_to_order', views.Meal_to_OrderView.as_view()),
    path('meal_categories', views.Meal_Categories.as_view()),
    path('departments', views.Departments.as_view()),
    path('active_orders', views.Active_orders.as_view()),
    path('tables', views.Tables.as_view()),
    path('statuses', views.Statuses.as_view()),
    path('service_persentage', views.Service_PersentageView.as_view()),
    path('orders/<int:pk>', views.OrdersDetail.as_view()),
    path('roles/<int:pk>', views.RolesDetail.as_view()),
    path('users/<int:pk>', views.UsersDetail.as_view()),
    path('checks/<int:pk>', views.ChecksDetail.as_view()),
    path('meals/<int:pk>', views.MealsDetail.as_view()),
    path('meals_meal_by_category/<int:pk>', views.Meals_meal_by_categoryDetail.as_view()),
    path('meal_categories_for_dep/<int:pk>', views.Meal_categories_for_DepDetail.as_view()),
    path('meal_to_order/<int:pk>', views.Meal_to_OrderDetail.as_view()),
    path('meal_categories/<int:pk>', views.Meal_Categories.as_view()),
    path('departments/<int:pk>', views.Departments.as_view()),
    # path('active_orders/<int:pk>', views.Active_orders.as_view()),
    path('tables/<int:pk>', views.Tables.as_view()),
    path('statuses/<int:pk>', views.Statuses.as_view()),
    # path('service_persentage/<int:pk>', views.Service_Persentage.as_view()),
    path('ordersget', views.OrdersGetView.as_view()),
    path('user', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns+=[
    path('api-auth/', include('rest_framework.urls'))
]