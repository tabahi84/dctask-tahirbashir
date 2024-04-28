from rest_framework import serializers
from django.forms.models import model_to_dict

from api.v1.models import Quote
from .customer_serializers import CustomerSerializer



class QuoteSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField()
    quote_id = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = Quote
        fields = ['quote_id', 'customer_id', 'customer', 'policy_type', 'premium', 'coverage', 'state']
    
    def __init__(self, *args, **kwargs):
        super(QuoteSerializer, self).__init__(*args, **kwargs)
        
        field_visibility_dict = {
            "OTHER": [],
            "UPDATE": ['quote_id', 'state'],
            "CREATE": ['customer_id', 'policy_type'],
        }
        
        request = self.context.get('request')
        visibility_key = "OTHER" if not request else "CREATE" if request.method == "POST" else "UPDATE" if request.method in ["PATCH"] else "OTHER"
        for field in self.fields:
            if field in field_visibility_dict[visibility_key]:
                self.fields[field].required = True
                self.fields[field].read_only = False
                self.fields[field].write_only = False
            else:
                self.fields[field].required = False
                self.fields[field].read_only = True
                self.fields[field].write_only = False
        self.fields['customer_id'].write_only = True
    
    def validate(self, data):
        instance = Quote(**data)
        instance.clean()
        m2d = model_to_dict(instance, exclude=['customer'])
        m2d['customer_id'] = instance.customer.id
        return m2d
