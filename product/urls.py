from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    AddToCartAPIView,
    CartDetailAPIView
)

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('filter/', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:id>/detail/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:id>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:id>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),

    path('add_to_cart/<int:user_id>/', AddToCartAPIView.as_view(), name='add-to-cart'),
    path('cart_detail/<int:user_id>/', CartDetailAPIView.as_view(), name='cart-detail'),
]