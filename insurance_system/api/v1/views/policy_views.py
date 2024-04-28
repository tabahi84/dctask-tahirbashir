from rest_framework import generics
from rest_framework import permissions, parsers
from drf_spectacular.utils import extend_schema, OpenApiParameter

from api.v1.models import Quote, Customer
from api.v1.serializers import PolicyDetailSerializer, CustomerPoliciesSerializer, PolicyDetailWOHistorySerializer



@extend_schema(
    tags=['Policy APIs'],
    parameters=[OpenApiParameter(name='customer_id', description='customer_id', required=True, type=int)]
)
class CustomerPoliciesListView(generics.RetrieveAPIView):
    parser_classes = []
    permission_classes = [permissions.AllowAny]
    
    queryset = Customer.objects.all()
    serializer_class = CustomerPoliciesSerializer

    def get_object(self):
        id = self.request.query_params.get('customer_id', None)
        if id:
            if not Customer.objects.filter(id=id).exists():
                raise ValueError(f"Customer having ID '{id}' does not exist")
            return Customer.objects.filter(id=id).first()
        raise AttributeError("customer_id url query parameter is missing")



@extend_schema(tags=['Policy APIs'])
class PolicyDetailWOHistoryView(generics.RetrieveAPIView):
    parser_classes = []
    permission_classes = [permissions.AllowAny]
    
    queryset = Quote.objects.all()
    serializer_class = PolicyDetailWOHistorySerializer



@extend_schema(tags=['Policy APIs'])
class PolicyDetailView(generics.RetrieveAPIView):
    parser_classes = []
    permission_classes = [permissions.AllowAny]
    
    queryset = Quote.objects.all()
    serializer_class = PolicyDetailSerializer