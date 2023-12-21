import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")
import django
import csv

# Set up Django
django.setup()

django.setup()  # Configure Django settings
from api.models import HealthInsaurenceData

def load_data():
    with open('HealthInsurance.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            HealthInsaurenceData.objects.create(**row)

if __name__ == '__main__':
    load_data()
