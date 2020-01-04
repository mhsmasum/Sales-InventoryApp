from django.urls import path
from . import views

urlpatterns = [
    path('', views.uom_list, name='uom_list'),
    path('create/', views.uom_create, name='uom_create'),
    path('update/<int:pk>', views.uom_update, name='uom_update'),
    path('delete/<int:pk>', views.uom_delete, name='uom_delete'),
    path('deletedetails/', views.uom_delete_details, name='uom_delete_details'),
]
