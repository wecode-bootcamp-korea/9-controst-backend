from django.db import models

class CounselCenter(models.Model):
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    center_type = models.CharField(max_length=20)
    name        = models.CharField(max_length=50)
    homepage_url = models.CharField(max_length=2000)
    phone_number = models.CharField(max_length=20)
    address      = models.CharField(max_length=1000)
    road_address = models.CharField(max_length=1000)
    is_trost_partner = models.BooleanField(default=False)
    partner_info     = models.CharField(max_length=2000)
    counseling_type  = models.CharField(max_length=100)

    class Meta:
        db_table = 'counselcenters'

# Create your models here.
