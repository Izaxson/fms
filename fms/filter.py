# import django_filters
# # from django_filters import DateFilter
# from fms.models import Received, Sent


# class ReceivedFilter(django_filters.FilterSet):    
#     start_date=DateFilter(field_name="created", lookup_expr='gte') 
#     end_date=DateFilter(field_name="created", lookup_expr='lte') 
#     class Meta:
#         model = Received
#         fields = '__all__'
#         exclude = ['odometer_start','odometer_close','profile','amount_collected','created',]