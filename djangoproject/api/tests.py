from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import HealthInsaurenceData

class HealthInsuranceAPITests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up initial data for tests
        HealthInsaurenceData.objects.create(age=25, sex='male', bmi=22.5, children=0, smoker='no', region='southwest', charges=3000.0)

    def test_get_all_data(self):
        # Test retrieving all health insurance data
        client = APIClient()
        url = reverse('api:GetAllData')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_by_id(self):
        # Test retrieving health insurance data by ID
        client = APIClient()
        data_id = HealthInsaurenceData.objects.first().id
        url = reverse('api:GetDataById', args=[data_id])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_smokers_by_region(self):
        # Test retrieving smokers in a specific region
        client = APIClient()
        url = reverse('api:GetSmokersByRegion', args=['southwest'])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_data(self):
        # Test creating new health insurance data
        client = APIClient()
        url = reverse('api:CreateData')
        data = {
            'age': 30,
            'sex': 'female',
            'bmi': 25.0,
            'children': 1,
            'smoker': 'no',
            'region': 'northeast',
            'charges': 4000.0
        }
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the created data in the database
        created_data = HealthInsaurenceData.objects.get(age=30)
        self.assertEqual(created_data.sex, 'female')

    def test_update_data_by_id(self):
        # Test updating health insurance data by ID
        client = APIClient()
        data_id = HealthInsaurenceData.objects.first().id
        url = reverse('api:UpdateDataById', args=[data_id])
        updated_data = {
            'age': 26,
            'bmi': 23.0,
        }
        response = client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the updated data in the database
        updated_data = HealthInsaurenceData.objects.get(id=data_id)
        self.assertEqual(updated_data.age, 26)

    def test_delete_data_by_id(self):
        # Test deleting health insurance data by ID
        client = APIClient()
        data_id = HealthInsaurenceData.objects.first().id
        url = reverse('api:DeleteDataById', args=[data_id])
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify that the data has been deleted
        with self.assertRaises(HealthInsaurenceData.DoesNotExist):
            HealthInsaurenceData.objects.get(id=data_id)

    def test_get_data_by_age_range(self):
        # Test retrieving health insurance data within a specified age range
        client = APIClient()
        url = reverse('api:GetDataByAgeRange', args=[20, 30])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_by_gender(self):
        # Test retrieving health insurance data by gender
        client = APIClient()
        url = reverse('api:GetDataByGender', args=['male'])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_filtered_data_by_criteria(self):
        # Test retrieving filtered health insurance data based on criteria
        client = APIClient()
        url = reverse('api:GetFilteredDataByCriteria', args=[20, 30, 20.0, 25.0, 'no'])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_average_charges_by_region(self):
        # Test retrieving average charges for health insurance data in a specific region
        client = APIClient()
        url = reverse('api:RetrieveAverageChargesByRegion', args=['southwest'])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
