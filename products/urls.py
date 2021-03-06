from django.urls import path

from products.views import home, add_product, product_detailed, buy_product, export_excel

urlpatterns = [
    path('', home, name='home'),
    path('add_product/', add_product, name='add_product'),
    path('detailed/<int:pk>', product_detailed, name='product_detailed'),
    path('buy_product/<int:pk>', buy_product, name='buy_product'),
    path('export_excel/<int:pk>', export_excel, name='export_excel')
]
