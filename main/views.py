from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class ProductAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
