
from rest_framework import viewsets, mixins
from . models import Product
from . serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


class ProductGenericViewSet(mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin, 
                            viewsets.GenericViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

