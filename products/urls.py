from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>/', views.product_category, name='product_category'),
    path('skincare/', views.skincare, name='skincare'),
    path('makeup/', views.makeup, name='makeup'),
    path('body-hair/', views.body_hair, name='body_hair'),
    path('special-offers/', views.special_offers, name='special_offers'),
]