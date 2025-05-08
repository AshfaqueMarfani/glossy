from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms, name='terms'),
    path('shipping-returns/', views.shipping_returns, name='shipping_returns'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('coming-soon/<str:feature>/', views.coming_soon, name='coming_soon_feature'),
]