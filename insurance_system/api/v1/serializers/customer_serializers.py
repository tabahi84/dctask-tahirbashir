from rest_framework import serializers
from django.forms.models import model_to_dict

from ..models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
    
    def validate(self, data):
        instance = Customer(**data)
        instance.clean()
        # https://stackoverflow.com/questions/21925671/convert-django-model-object-to-dict-with-all-of-the-fields-intact
        return model_to_dict(instance)

