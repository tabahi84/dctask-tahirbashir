from rest_framework import generics
from rest_framework import permissions, parsers

from api.v1.models import Quote, Customer
from api.v1.serializers import CustomerPoliciesSerializer, PolicyDetailSerializer



class CustomerPoliciesListView(generics.RetrieveAPIView):
    parser_classes = []
    permission_classes = [permissions.AllowAny]
    
    queryset = Customer.objects.all()
    serializer_class = CustomerPoliciesSerializer

    def get_object(self):
        id = self.request.query_params.get('customer_id', None)
        if id:
            return Customer.objects.filter(id=id).first()
        return Customer.objects.none()




class PolicyDetailView(generics.RetrieveAPIView):
    parser_classes = []
    permission_classes = [permissions.AllowAny]
    
    queryset = Quote.objects.all()
    serializer_class = PolicyDetailSerializer
