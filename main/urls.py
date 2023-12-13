from django.urls import path
from .views import CategoryAPIView, ProductAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category_list'),
    path('products/', ProductAPIView.as_view(), name='category_products')
]
