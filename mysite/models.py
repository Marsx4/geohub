from django.db import models
from django.utils import timezone


class Service(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name=models.CharField(max_length=200,unique=True)
    date_joined=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Facility(models.Model):
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    province=models.CharField(max_length=200,choices=[('Harare','harare'),('Chivi','Chivi')])
    district=models.CharField(max_length=200,choices=[('Harare','harare'),('Chivi','Chivi')])
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.organization.name}/{self.district}/{self.province}"

    class Meta:
        verbose_name_plural="Facilities"


# class Data(models.Model):
#     lon=models.FloatField(max_length=10)
#     lat=models.FloatField(max_length=10)
#     cso_name=models.CharField(max_length=200)
#     phone=models.CharField(max_length=200)
#     year_joined=models.CharField(max_length=10)
#     started_operation=models.CharField(max_length=200)
#     ended_operation=models.CharField(max_length=200)
#     provinces=models.CharField(max_length=10000)
#     districts=models.CharField(max_length=10000)
#     focus=models.CharField(max_length=10000)
#     support_total=models.CharField(max_length=10000)
#     service_type=models.CharField(max_length=200)
#     support_2018=models.CharField(max_length=200)
#     support_2019=models.CharField(max_length=200)
#     support_2020=models.CharField(max_length=200)
#     support_2021=models.CharField(max_length=200)
#     target_beneficiary=models.CharField(max_length=200)
