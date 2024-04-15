from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
# from api.authentication import TokenAuthentication ##(already set as default in settings.py)
from . models import Product
from . serializers import ProductSerializer, DetailSerializer


class ProductListCreateAPIView(# StaffEditorPermissionMixin,
                               UserQuerySetMixin,
                               generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        
        serializer.save(user=self.request.user, content=content)
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     print(user)

    #     if user.is_authenticated:
    #         return qs.filter(user=user)
        
    #     return Product.objects.none()
        

class ProductDetailAPIView(# StaffEditorPermissionMixin,
                           UserQuerySetMixin,
                           generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = DetailSerializer
    

class ProductUpdateAPIView(StaffEditorPermissionMixin,
                           UserQuerySetMixin,
                           generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = DetailSerializer

    def perform_update(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        
        serializer.save(user=self.request.user, content=content)


class ProductDeleteAPIView(StaffEditorPermissionMixin,
                           UserQuerySetMixin,
                           generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = DetailSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    

class ProductMixinView(StaffEditorPermissionMixin,
                       UserQuerySetMixin,
                       mixins.ListModelMixin, 
                       mixins.RetrieveModelMixin, 
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin, 
                       generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        
        serializer.save(user=self.request.user, content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        
        serializer.save(user=self.request.user, content=content)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

######################################################################

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        
        return Response(data)

    elif method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')

            if content is None:
                content = title
            
            serializer.save(content=content)

            data = serializer.data 
            print(data)   

            return Response(data)
        
        return Response({'detail':'bad/invalid request'}, status=400)