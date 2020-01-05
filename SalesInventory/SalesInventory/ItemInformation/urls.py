from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemInformation_list, name='ItemInformation_list'),
    path('create/', views.ItemInformation_create, name='ItemInformation_create'),
    path('update/<int:pk>', views.ItemInformation_update, name='ItemInformation_update'),
    path('delete/<int:pk>', views.ItemInformation_delete, name='ItemInformation_delete'),
]
