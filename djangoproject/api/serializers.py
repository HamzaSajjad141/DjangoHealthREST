from rest_framework import serializers
from .models import HealthInsaurenceData

class HealthInsaurenceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsaurenceData
        fields = '__all__'
