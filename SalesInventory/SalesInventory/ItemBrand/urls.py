from django.urls import path
from . import views

urlpatterns = [
    path('', views.itembrand_list, name='itembrand_list'),
    path('create/', views.itembrand_create, name='itembrand_create'),
    path('update/<int:pk>', views.itembrand_update, name='itembrand_update'),
    path('delete/<int:pk>', views.itembrand_delete, name='itembrand_delete'),
]
