
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import Product


# def validate_title(value):
#         query_set = Product.objects.filter(title__iexact=value)

#         if query_set:
#             raise serializers.ValidationError(f'Title already exist in products!')
        
#         return value

def validate_title_no_value(value):
        
        if 'hello' in value.lower():
              raise serializers.ValidationError(f'"hello" not allowed in title!!')
        
        return value 

unique_product_title = UniqueValidator(Product.objects.all(), lookup='iexact')