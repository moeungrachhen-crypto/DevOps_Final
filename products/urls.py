from django.urls import path
from .views import (
    home,
    product_list,
    product_detail,
    category_products
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'products/',
        product_list,
        name='product_list'
    ),

    path(
        'product/<int:id>/',
        product_detail,
        name='product_detail'
    ),

    path(
        'category/<int:category_id>/',
        category_products,
        name='category_products'
    ),

]