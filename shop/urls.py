from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка (Категорії)
    path('', views.categories_view, name='categories'),
    
    # 1. READ (Список товарів)
    path('products/', views.ProductListView.as_view(), name='products'),
    
    # 2. CREATE (Створення товару)
    path('products/create/', views.create_product, name='product-create'),
    
    # 3. DETAIL (Детальний перегляд одного товару)
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    
    # 4. UPDATE (Редагування товару)
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    
    # 5. DELETE (Видалення товару)
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]