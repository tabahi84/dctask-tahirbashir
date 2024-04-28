from rest_framework import serializers

from api.v1.models import Customer, Quote, QuoteHistory

class PolicyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteHistory
        fields = ['state', 'updated_at']



class PolicyDetailSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    history = PolicyHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'customer_id', 'customer_name', 'policy_type', 'premium', 'coverage', 'state', 'history']
    
    def get_customer_name(self, obj):
        return str(obj.customer) if obj.customer else None



class CustomerPoliciesSerializer(serializers.ModelSerializer):
    policies = PolicyDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'dob', 'policies']
