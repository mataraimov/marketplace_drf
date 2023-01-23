from django.urls import path
from .views import VendorRegisterView, CustomerRegisterView, VendorListApiView, CustomerListApiView, LoginView,VendorApiView,CustomerApiView

urlpatterns = [
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor-register'),
    path('customer/register/', CustomerRegisterView.as_view(), name='customer-register'),
    path('vendor/list/', VendorListApiView.as_view(), name='vendor-list'),
    path('vendor/<int:id>/', VendorApiView.as_view(), name='vendor-detail'),
    path('customer/<int:id>/', CustomerApiView.as_view(), name='customer-detail'),
    path('customer/list/', CustomerListApiView.as_view(), name='vendor-list'),
    path('login/',LoginView.as_view(),name='login')
]