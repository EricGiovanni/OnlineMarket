from django.urls import path

from . import views

app_name = 'product_app'

urlpatterns = [
    path(
        'product_register/',
        views.RegisterView.as_view(),
        name='product_register'
    ),
    path(
        'product_list_seller/',
        views.ProductsSellerView.as_view(),
        name='product_list_seller'
    ),
]

