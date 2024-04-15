
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_alt_view, name='list_create_products'),
    # path('', views.ProductMixinView.as_view(), name='list_create_products'),
    path('', views.ProductListCreateAPIView.as_view(), name='list-products'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='view-products'),
    path('<int:pk>/update/', views.ProductMixinView.as_view(), name='update-products'),
    path('<int:pk>/delete/', views.ProductMixinView.as_view(), name='delete-products'),
]
