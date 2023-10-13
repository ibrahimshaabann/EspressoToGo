from rest_framework import filters
from .models import Attendance

class AttendanceOutTimeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):        
        return queryset.filter(out_time__isnull=True)