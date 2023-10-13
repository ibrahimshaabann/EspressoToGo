from django.contrib import admin
from .models import Cost
from .views import BenefitsViewSet
from decimal import Decimal
from orders.models import Order
from django.urls import path
from django.shortcuts import render
@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'date' , 'type','user']
    list_filter = ['date','user','type',]
    search_fields = ['user__full_name','description',]