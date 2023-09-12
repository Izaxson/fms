import django_filters
from django_filters import DateFilter
from fms.models import Received, Sent


class SentFilter(django_filters.FilterSet):    
    start_date=DateFilter(field_name="date_created", lookup_expr='gte') 
    end_date=DateFilter(field_name="date_created", lookup_expr='lte') 
    class Meta:
        model = Sent
        fields = '__all__'
        exclude = ['file',]


class ReceivedFilter(django_filters.FilterSet):    
    start_date=DateFilter(field_name="date_created", lookup_expr='gte') 
    end_date=DateFilter(field_name="date_created", lookup_expr='lte') 
    class Meta:
        model = Received
        fields = '__all__'
        exclude = ['file',]        