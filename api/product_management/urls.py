from django.urls import path
from .products.views import ProductsAPIView
from .products.id.views import ProductsIdAPIView
from .categories.views import CategoriesAPIView
from .categories.id.views import CategoriesIdAPIView


urlpatterns = [
    path('products', ProductsAPIView.as_view()),
    path('products/<int:product_id>', ProductsIdAPIView.as_view()),
    path('categories', CategoriesAPIView.as_view()),
    path('categories/<int:category_id>', CategoriesIdAPIView.as_view()),
]
