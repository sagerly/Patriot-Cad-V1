# serializers.py

from rest_framework import serializers
from .models import CurrentCall, Civilian

class CurrentCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentCall
        fields = ['id', 'description', 'time_of_call', 'priority']

class CivilianRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civilian
        fields = ['first_name', 'last_name', 'date_of_birth']
        # Add any other fields you require for registration