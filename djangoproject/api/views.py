from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HealthInsaurenceData
from .serializers import HealthInsaurenceDataSerializer

# Example endpoints (replace with your specific requirements)
class GetAllData(APIView):
    def get(self, request):
        data = HealthInsaurenceData.objects.all()
        serializer = HealthInsaurenceDataSerializer(data, many=True)
        return Response(serializer.data)

class GetDataById(APIView):
    def get(self, request, id):
        try:
            data = HealthInsaurenceData.objects.get(id=id)
        except HealthInsaurenceData.DoesNotExist:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HealthInsaurenceDataSerializer(data)
        return Response(serializer.data)


class GetSmokersByRegion(APIView):
    def get(self, request, region):
        data = HealthInsaurenceData.objects.filter(smoker='yes', region=region)
        serializer = HealthInsaurenceDataSerializer(data, many=True)
        return Response(serializer.data)


