from django.shortcuts import render
from .models import EquipmentAndItems , Brands , Store
from .serializers import EquipmentAndItemsSerializer , BrandsSerializer , StoreSerializer
from rest_framework import viewsets

class EquipmentAndItemsViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentAndItemsSerializer
    queryset = EquipmentAndItems.objects.all()

class BrandsViewSet(viewsets.ModelViewSet):
    serializer_class = BrandsSerializer
    queryset = Brands.objects.all()

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


# Create your views here.
