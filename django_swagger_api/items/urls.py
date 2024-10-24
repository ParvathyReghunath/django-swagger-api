from django.contrib import admin
from django.urls import path
from .views import ItemListCreate,ItemDetail


urlpatterns = [
    path('items/',ItemListCreate.as_view(),name='item_list'),
    path('items/<int:pk>',ItemDetail.as_view(),name='item_detail'),

]