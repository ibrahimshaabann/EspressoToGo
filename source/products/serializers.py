from rest_framework import serializers
from .models import Category, Menu



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    # this category attribute shows the name of the category object related to the menu item 
    # using serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Menu
        fields = '__all__'