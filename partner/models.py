from django.db import models

class Counselor(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES= [(GENDER_MALE, "Male"), (GENDER_FEMALE, "Female")]
    LEVEL_MASTER = "M"
    LEVEL_PROFESSIONAL = "P"
    LEVEL_GENERAL = "G"
    LEVEL_CHOICES = [(LEVEL_MASTER, "Master"), (LEVEL_PROFESSIONAL, "Professional"), (LEVEL_GENERAL, "General")]

    name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    counsel_count = models.IntegerField(default=0)
    introduction = models.CharField(max_length=1000)
    is_counsel_gt_150 = models.IntegerField(default=0)
    profile_image_url = models.URLField(max_length=200)

    class Meta:
        db_table = "counselors"

class Theme(models.Model):
    theme = models.CharField(max_length=10)

    class Meta:
        db_table = "themes"

class Counselor_Theme(models.Model):
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    class Meta:
        db_table = "counselors_themes"

class Counsel_Kind(models.Model):
    kind = models.CharField(max_length=20)

    class Meta:
        db_table = "counsel_kinds"

class Counselor_Counsel_kind(models.Model):
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    counsel_kind = models.ForeignKey(Counsel_Kind, on_delete=models.CASCADE)

    class Meta:
        db_table = "counselors_counsel_kinds"

class Duration(models.Model):
    duration = models.CharField(max_length=30)

    class Meta:
        db_table = "durations"



