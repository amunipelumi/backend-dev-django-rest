from rest_framework import generics
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from . import client


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        result = Product.objects.none()
        
        if q:
            user = None

            if self.request.user.is_authenticated:
                user = self.request.user

            result = qs.search(q, user=user)

        return result


class AlgoliaSearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None

        if request.user.is_authenticated:
            user = request.user.username

        index_name = request.GET.get('i')
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != '0'
        tags = request.GET.get('tags')

        print(f'user-->{user}, index_name-->{index_name}, query-->{query}, public-->{public}, tags-->{tags}')
        
        if index_name:
            if query:
                results = client.perform_search(index_name, query, tags=tags, user=user, public=public)
                return Response(results)
        
        return Response('', status=400)
        