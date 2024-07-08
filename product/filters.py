import django_filters
from .models import Category



class CategoryFilter(django_filters.FilterSet):
    name =  name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    # description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name',]
