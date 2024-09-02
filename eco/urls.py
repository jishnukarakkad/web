from . import views
from django . urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.product,name='products'),
    path('cart/',views.cart,name='cart.html'),
    path('review/',views.review,name='review'),
]