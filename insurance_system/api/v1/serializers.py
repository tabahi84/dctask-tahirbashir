from rest_framework import status, serializers
from rest_framework.response import Response

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
    # def create(self, validated_data):
    #     if Customer.objects.filter(first_name=validated_data['first_name'], last_name=validated_data['last_name']).exists():
    #         return Response(data={"message": "Customer with same first and last name already exists"}, status=status.HTTP_400_BAD_REQUEST)
    #         # return Response(data={"message": "Customer with same first and last name already exists"}, status=status.HTTP_400_BAD_REQUEST)
    #     return Customer.objects.create(**validated_data)