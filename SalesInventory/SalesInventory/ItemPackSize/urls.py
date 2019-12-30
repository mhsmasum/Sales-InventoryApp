from django.urls import path
from ItemPackSize import views

urlpatterns = [
    path('', views.packsize_list, name='packsize_list'),
    path('create/', views.packsize_create, name='packsize_create'),
    path('update/<int:pk>', views.packsize_update, name='packsize_update'),
    path('delete/<int:pk>', views.packsize_delete, name='packsize_delete'),
    
]
