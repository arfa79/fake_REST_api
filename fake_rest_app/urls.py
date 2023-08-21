from django.urls import path
from .views import ItemList

urlpatterns = [
    path('api/items/', ItemList.as_view(), name='item-list'),
]
