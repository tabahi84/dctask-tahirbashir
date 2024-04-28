from rest_framework import serializers

from api.v1.serializers import CustomerSerializer
from api.v1.models import Customer, Quote, QuoteHistory

class PolicyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteHistory
        fields = ['state', 'updated_at']
class PolicyDetailSerializer(serializers.ModelSerializer):
    """
    This serializer is used to show policy history when activated using policies/<policy_id>/history url endpoint
    """
    customer_name = serializers.SerializerMethodField()
    history = PolicyHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'customer_id', 'customer_name', 'policy_type', 'premium', 'coverage', 'state', 'history']
    
    def get_customer_name(self, obj):
        return str(obj.customer) if obj.customer else None



###################################################################################
# Serializer for policy and customer details for policies/<policy_id> url endpoint
###################################################################################
class PolicyDetailWOHistorySerializer(serializers.ModelSerializer):
    """
    This serializer is used to show policy detail when activated using policies/<policy_id> url endpoint
    """
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Quote
        fields = ['id', 'policy_type', 'premium', 'coverage', 'state', 'customer']



###################################################################
# Serializers for customer-policies listing based on ?customer_id
###################################################################
class CustomerPolicyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'policy_type', 'premium', 'coverage', 'state']
    
    def get_customer_name(self, obj):
        return str(obj.customer) if obj.customer else None
class CustomerPoliciesSerializer(serializers.ModelSerializer):
    """
    This serializer is used to show customer policies when activated using policies?customer_id url endpoint
    """
    policies = CustomerPolicyDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'dob', 'policies']
