from django.urls import path
from ItemGroup import views

urlpatterns = [
    path('', views.itemGroup_list, name='itemGroup_list'),
    path('create/', views.itemGroup_create, name='itemGroup_create'),
    path('update/<int:pk>', views.itemGroup_update, name='itemGroup_update'),
    path('delete/<int:pk>', views.itemGroup_delete, name='itemGroup_delete'),
    
]
