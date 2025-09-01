from rest_framework import serializers
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'position', 'department', 'start_date']
        
    # def create(self, validated_data):
    #     return