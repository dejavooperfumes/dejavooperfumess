from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path(r'^create/$', views.order_create, name='order_create'),
    #path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
    path("sucess/", views.sucess, name="sucess"),
    
]