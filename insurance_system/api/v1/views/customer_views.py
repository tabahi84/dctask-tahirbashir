from rest_framework import generics
from rest_framework import permissions, parsers
from drf_spectacular.utils import extend_schema

from api.v1.models import Customer
from api.v1.serializers import CustomerSerializer

@extend_schema(tags=['Customer APIs'])
class CustomerCreateView(generics.CreateAPIView):
    parser_classes = [parsers.JSONParser]
    permission_classes = [permissions.AllowAny]
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
