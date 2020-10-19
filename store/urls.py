from django.urls import path
from . import views
from .middlewares.auth import auth_middleware

urlpatterns=[
    path('',views.home,name='homepage'),
    path('signup',views.signup),
    path('login',views.login,name='login'),
    path('logout',views.logout),
    path('cart',views.cart),
    path('checkout',views.checkout),
    path('orders',views.order_history)
]

def checkout(request):
   pass