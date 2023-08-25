from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# API views
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# index view to render the HTML template
def index(request):
    queryset = Item.objects.all()
    return render(request, 'index.html' , {'items' : request })
def custom_404(request, exception):
    return render(request, '404.html', status=404)
