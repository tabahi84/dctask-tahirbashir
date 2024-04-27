from rest_framework import generics
from rest_framework import permissions, parsers

from api.v1.models import Customer
from api.v1.serializers import CustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    parser_classes = [parsers.JSONParser]
    permission_classes = [permissions.AllowAny]
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
