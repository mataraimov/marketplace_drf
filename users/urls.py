from django.urls import path
from .views import VendorRegisterView

urlpatterns = [
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor-register')

]