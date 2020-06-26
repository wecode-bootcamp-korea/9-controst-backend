from django.db import models

class Counselor(models.Model):
    name                    = models.CharField(max_length=50)
    gender                  = models.CharField(max_length=10)
    level                   = models.ForeignKey('Level', on_delete=models.CASCADE)
    counsel_count           = models.IntegerField(default=0)
    introduction            = models.CharField(max_length=1000)
    is_counsel_count_gt_150 = models.BooleanField(default=False)
    profile_image_url       = models.URLField(max_length=2000)
    theme                   = models.ManyToManyField('Theme', through = 'CounselorTheme')
    kind                    = models.ManyToManyField('Kind', through = 'CounselorKind')

    class Meta:
        db_table = "counselors"

class Level(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "levels"

class Theme(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "themes"

class CounselorTheme(models.Model):
    counselor = models.ForeignKey('Counselor', on_delete=models.CASCADE)
    theme     = models.ForeignKey('Theme', on_delete=models.CASCADE)

    class Meta:
        db_table = 'counselor_themes'

class Kind(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "kinds"

class CounselorKind(models.Model):
    counselor = models.ForeignKey('Counselor', on_delete=models.CASCADE)
    kind      = models.ForeignKey('Kind', on_delete=models.CASCADE)

    class Meta:
        db_table = 'counselor_kinds'

class Duration(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "duration"

class Product(models.Model):
    level    = models.ForeignKey('Level', on_delete = models.CASCADE)
    kind     = models.ForeignKey('Kind', on_delete=models.CASCADE)
    duration = models.ForeignKey('Duration', on_delete=models.CASCADE)
    price    = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'products'

