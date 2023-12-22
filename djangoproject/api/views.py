from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HealthInsaurenceData
from .serializers import HealthInsaurenceDataSerializer
from django.db.models import Avg

# endpoints
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



class CreateData(APIView):
    def post(self, request):
        serializer = HealthInsaurenceDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDataById(APIView):
    def put(self, request, id):
        try:
            data = HealthInsaurenceData.objects.get(id=id)
        except HealthInsaurenceData.DoesNotExist:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HealthInsaurenceDataSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteDataById(APIView):
    def delete(self, request, id):
        try:
            data = HealthInsaurenceData.objects.get(id=id)
        except HealthInsaurenceData.DoesNotExist:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GetDataByAgeRange(APIView):
    def get(self, request, min_age, max_age):
        try:
            min_age = int(min_age)
            max_age = int(max_age)
        except ValueError:
            return Response({"error": "Invalid age range. Please provide valid integers for min_age and max_age."},
                            status=status.HTTP_400_BAD_REQUEST)

        if min_age < 0 or max_age < 0:
            return Response({"error": "Age values cannot be negative."},
                            status=status.HTTP_400_BAD_REQUEST)

        if max_age < min_age:
            return Response({"error": "max_age must be greater than or equal to min_age."},
                            status=status.HTTP_400_BAD_REQUEST)

        data = HealthInsaurenceData.objects.filter(age__gte=min_age, age__lte=max_age)
        serializer = HealthInsaurenceDataSerializer(data, many=True)
        return Response(serializer.data)


class GetDataByGender(APIView):
    def get(self, request, gender):
        if gender.lower() not in ['male', 'female']:
            return Response({"error": "Invalid gender. Please provide 'male' or 'female'."},
                            status=status.HTTP_400_BAD_REQUEST)

        data = HealthInsaurenceData.objects.filter(sex=gender.lower())
        serializer = HealthInsaurenceDataSerializer(data, many=True)
        return Response(serializer.data)




class GetFilteredDataByCriteria(APIView):
    def get(self, request, min_age, max_age, min_bmi, max_bmi, smoking_status):
        try:
            min_age = int(min_age)
            max_age = int(max_age)
            min_bmi = float(min_bmi)
            max_bmi = float(max_bmi)
        except (ValueError, TypeError):
            return Response({"error": "Invalid input. Please provide valid integers for age and floats for BMI."},
                            status=status.HTTP_400_BAD_REQUEST)

        if min_age < 0 or max_age < 0 or min_bmi < 0 or max_bmi < 0:
            return Response({"error": "Age and BMI values cannot be negative."},
                            status=status.HTTP_400_BAD_REQUEST)

        if max_age < min_age:
            return Response({"error": "max_age must be greater than or equal to min_age."},
                            status=status.HTTP_400_BAD_REQUEST)

        if max_bmi < min_bmi:
            return Response({"error": "max_bmi must be greater than or equal to min_bmi."},
                            status=status.HTTP_400_BAD_REQUEST)

        if smoking_status.lower() not in ['yes', 'no']:
            return Response({"error": "Invalid smoking status. Please provide 'yes' or 'no'."},
                            status=status.HTTP_400_BAD_REQUEST)

        data = HealthInsaurenceData.objects.filter(
            age__gte=min_age, age__lte=max_age,
            bmi__gte=min_bmi, bmi__lte=max_bmi,
            smoker=smoking_status.lower()
        )

        serializer = HealthInsaurenceDataSerializer(data, many=True)
        return Response(serializer.data)







class RetrieveAverageChargesByRegion(APIView):
    def get(self, request, region):
        try:
            average_charges = HealthInsaurenceData.objects.filter(region=region).aggregate(Avg('charges'))['charges__avg']
        except ZeroDivisionError:
            return Response({"error": "No data available for the specified region."},
                            status=status.HTTP_404_NOT_FOUND)
        
        if average_charges is not None:
            return Response({"average_charges": average_charges})
        else:
            return Response({"error": "No data available for the specified region."},
                            status=status.HTTP_404_NOT_FOUND)
