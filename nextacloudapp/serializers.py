from rest_framework import serializers
from .models import EquipmentAndItems , Brands , Store

class EquipmentAndItemsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EquipmentAndItems
        fields = '__all__'

class BrandsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brands
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
