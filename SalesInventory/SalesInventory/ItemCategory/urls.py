from django.urls import path
from . import views

urlpatterns = [
    path('', views.itemcategory_list, name='itemcategory_list'),
    path('create/', views.itemcategory_create, name='itemcategory_create'),
    path('update/<int:pk>', views.itemcategory_update, name='itemcategory_update'),
    path('delete/<int:pk>', views.itemcategory_delete, name='itemcategory_delete'),
]
