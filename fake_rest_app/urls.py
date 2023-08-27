from django.urls import path
from . import views

handler404 = 'fake_rest_app.views.custom_404'
urlpatterns = [
    # API views
    path('api/items/', views.ItemList.as_view(), name='item-list'),

    # Index view for rendering the HTML template
    path('', views.index, name='index'),
    
    path('404/', views.custom_404, name='custom-404'),
]
