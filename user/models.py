from django.db import models
from partner.models import (
    Counselor,
    Level,
    Theme,
    CounselorTheme,
    Kind,
    CounselorKind,
    Duration,
    Product
)

class User(models.Model):
    email      = models.EmailField(max_length = 255)
    password   = models.CharField(max_length = 200)
    nickname   = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "users"

class History(models.Model):
    product    = models.ForeignKey(Product, on_delete = models.PROTECT)
    user       = models.ForeignKey(User, on_delete = models.PROTECT)
    counselor  = models.ForeignKey(Counselor, on_delete = models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "histories"

class Like(models.Model):
    user      = models.ForeignKey(User, on_delete = models.CASCADE)
    counselor = models.ForeignKey(Counselor, on_delete = models.CASCADE)

    class Meta:
        db_table = "likes"
# Create your models here.
