# filepath: /home/sugesh/Desktop/django.project/organicmart/onlinemart/urls.py
from django.urls import path
from .views import home,product,about, contact,buy_now, confirm_purchase

urlpatterns = [
    path('', home, name='admin'),  # Root URL
    path('home/', home, name='home'),  # /home/ URL
    path('product/',product, name='product'),  # /product/ URL
    path('about/', about, name='about'),  # /about/ URL
    path('contact/', contact, name='contact'),  # /contact/ URL
    path('buy-now/',buy_now, name='buy_now'),
    path('confirm-purchase/',confirm_purchase, name='confirm_purchase'),
    path('thank-you/', confirm_purchase, name='thank_you'),  # /thank-you/ URL
]
