from django.db import models


class District_Mapping(models.Model):
    state_id = models.IntegerField()
    district_id = models.IntegerField()
    district_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
