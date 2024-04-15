from django.urls import path
from . views import SearchListView, AlgoliaSearchListView


urlpatterns = [
    # path('', SearchListView.as_view(), name='search'),
    path('', AlgoliaSearchListView.as_view(), name='search')
]