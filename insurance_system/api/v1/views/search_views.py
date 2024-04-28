from django.db.models import Q

from rest_framework import filters
from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter

from api.v1.models import Customer
from api.v1.serializers import CustomerPoliciesSerializer

@extend_schema(
    tags=['Search APIs'],
    parameters=[
        OpenApiParameter(name='name', description='String to match from first & last names', required=False, type=str),
        OpenApiParameter(name='policy', description='String to match from customer policy_types', required=False, type=str),
        OpenApiParameter(name='year', description='Year component of dob to match', required=False, type=int),
    ]
)
class CustomerSearchAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerPoliciesSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.query_params.get('name', None)
        year_query = self.request.query_params.get('year', None)
        policy_query = self.request.query_params.get('policy', None)

        if not (name_query or year_query or policy_query):
            raise AttributeError("Please provide either name, year and/or policy url query parameter for matching")

        if name_query is not None:
            queryset = queryset.filter(
                Q(first_name__icontains=name_query) | 
                Q(last_name__icontains=name_query)
            )

        if year_query is not None:
            queryset = queryset.filter(dob__year=year_query)

        if policy_query is not None:
            queryset = queryset.filter(Q(policies__policy_type__icontains=policy_query))

        return queryset
