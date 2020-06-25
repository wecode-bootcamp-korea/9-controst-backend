from django.db import models

class Counselor(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES= [(GENDER_MALE, "Male"), (GENDER_FEMALE, "Female")]

    name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    counsel_count = models.IntegerField(default=0)
    introduction = models.CharField(max_length=1000)
    is_counsel_gt_150 = models.IntegerField(default=0)
    profile_image_url = models.URLField(max_length=200)
    counsel_themes = models.ManyToManyField('Theme')
    counsel_kinds = models.ManyToManyField('CounselKind')

    class Meta:
        db_table = "counselors"

class Level(models.Model):
    level = models.CharField(max_length=19)

    class Meta:
        db_table = "levels"

class Theme(models.Model):
    theme = models.CharField(max_length=9)

    class Meta:
        db_table = "themes"

class CounselKind(models.Model):
    counsel_kind = models.CharField(max_length=20)

    class Meta:
        db_table = "counsel_kinds"

class Duration(models.Model):
    duration = models.CharField(max_length=30)

    class Meta:
        db_table = "durations"

class Product(models.Model):
    level = models.ForeignKey(Level, on_delete = models.CASCADE)
    counsel_kind = models.ForeignKey(CounselKind, on_delete=models.CASCADE)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'products'


