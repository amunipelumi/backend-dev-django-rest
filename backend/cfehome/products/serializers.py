
from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserSerializer
from . models import Product
from . validators import validate_title_no_value, unique_product_title

class ProductSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(source='user', read_only=True)
    title = serializers.CharField(validators=[validate_title_no_value, unique_product_title])
    view = serializers.HyperlinkedIdentityField(view_name='view-products', lookup_field='pk')

    class Meta:
        model = Product
        fields = [
            'owner',
            'title', 
            'view',
            ]
        
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj
    
    #     return Product.objects.create(**validated_data)
    
    def get_my_discount(self, obj):
        try:
            return obj.discount()
        except:
            return None 
  

class DetailSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(validators=[validate_title_no_value, unique_product_title])
    my_discount = serializers.SerializerMethodField(read_only=True)
    update = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'email',
            'id',
            'title', 
            'content', 
            'price',
            'sale_price',
            'my_discount',
            'public',
            'update',
            ]
    
    def get_my_discount(self, obj):
        try:
            return obj.discount()
        except:
            return None 
    
    def get_update(self, obj):
        request = self.context.get('request')

        if request is None:
            return None
        
        return reverse('update-products', kwargs={'pk':obj.pk}, request=request)


# class MainSerializer1(serializers.Serializer):
#     owner = UserSerializer(source='user', read_only=True)
#     product = ProductSerializer(source='user.product_set.all', read_only=True, many=True)


# class MainSerializer2(serializers.Serializer):
#     owner = UserSerializer(source='user', read_only=True)
#     detail = DetailSerializer(source='user.product_set.all', read_only=True, many=True)
