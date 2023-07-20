import django_filters
from .models import Order
from django.forms import TextInput

class OrderFilter(django_filters.FilterSet):
    date = django_filters.DateFilter()
    class Meta:
        model = Order
        fields = ['name', 'id', 'date']