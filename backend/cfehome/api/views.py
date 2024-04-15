import json
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view(['GET'])
@api_view(['POST'])
def api_home(request, *args, **kwargs):

    # instance = Product.objects.all().order_by('?').first()
    # data = {}

    # if instance:
        # data['id'] = model_data.id
        # data['tile'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # data = model_to_dict(instance, fields=[
        #     'id', 
        #     'title', 
        #     'price', 
        #     'sale_price', 
        #     'discount'
        # ])

        # data = ProductSerializer(instance).data
        # data = request.data
    
    # return JsonResponse(data) 

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        data = serializer.data    


    return Response(data)