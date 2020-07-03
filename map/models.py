from django.db import models

class CounselCenter(models.Model):
    longitude        = models.DecimalField(max_digits=22, decimal_places=16)
    latitude         = models.DecimalField(max_digits=22, decimal_places=16)
    center_type      = models.CharField(max_length=20, null=True, blank=True)
    name             = models.CharField(max_length=50, null=True, blank=True)
    homepage_url     = models.CharField(max_length=2000,null=True, blank=True)
    phone_number     = models.CharField(max_length=20,null=True, blank=True)
    address          = models.CharField(max_length=1000,null=True, blank=True)
    road_address     = models.CharField(max_length=1000,null=True, blank=True)
    is_trost_partner = models.BooleanField(default=False,null=True, blank=True)
    partner_info     = models.CharField(max_length=2000,null=True, blank=True)
    counseling_type  = models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        db_table = 'counsel_centers'

