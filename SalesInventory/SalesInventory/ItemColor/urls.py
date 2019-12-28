from django.urls import path
from . import views

urlpatterns = [
    path('', views.itemcolor_list, name='itemcolor_list'),
    path('create/', views.itemcolor_create, name='itemcolor_create'),
    path('update/<int:pk>', views.itemcolor_update, name='itemcolor_update'),
    path('delete/<int:pk>', views.itemcolor_delete, name='itemcolor_delete'),
]
