from  django.urls  import path
from . import views

urlpatterns = [
    path('', views.store,name="store"),
    path('cart/', views.cart,name="cart"),
    path('displayProduct/<int:id>', views.displayProduct,name="displayProduct"),  
    path('processOrder/', views.processOrder,name="processOrder"),
    path('checkout/', views.checkout,name="checkout")    
]