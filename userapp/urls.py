from django.urls import path
from userapp.views import *

urlpatterns = [
    path('hello',hello_world,name='hello_world'),
    path('category/list',category_list,name='category_list'),
    path('product/list',product_list,name='product_list'),
    path('product/add', product_add, name='product-add'),
    path('category/<int:category_id>/view/', category_view, name='category-view'),
    path('product/<int:product_id>/view/', product_view, name='product-view'),
    path('category/<int:category_id>/delete/', category_delete, name='category-delete'),
    # path('category/<int:category_id>/edit/', category_edit, name='category-edit'),
    path('category/<int:category_id>/edit/', category_edit, name='category-edit'),
    path('category/<int:category_id>/update/', category_update, name='category-update'),
    path('product/<int:product_id>/update/', product_update, name='product-update'),
            
]
