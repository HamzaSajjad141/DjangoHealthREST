# Generated by Django 5.0 on 2023-12-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthInsaurenceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('bmi', models.FloatField()),
                ('children', models.IntegerField()),
                ('smoker', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=15)),
                ('charges', models.FloatField()),
            ],
        ),
    ]