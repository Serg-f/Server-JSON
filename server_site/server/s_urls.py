from django.urls import path

from server.views import *

urlpatterns = [
    path('', index, name='home'),
    path('orders', get_all_orders, name='get_orders'),
    path('order', get_order, name='get_order'),

]
