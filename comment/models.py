from django.db import models
from partner.models import Counselor, Theme
from users.models import History

class Review(models.Model):
    history = models.ForeignKey('History', on_delete = models.PROTECT)
    created_at =  models.DateTimeField(auto_now_add = True)
    score = models.FloatField(decimal_places=1, defualt=2.5)
    comment = models.CharField(max_length=10000)
    theme = models.ManytoManyField('Theme', through='ReviewThemes', related_name = 'review') 

    class Meta:
        db_table = 'reviews'

class ReviewTheme(models.Model):
    review = models.ForeignKey('Review', on_delete = models.CASCADE)
    theme = models.ForiengKey('Themes', on_delete = models.CASCADE)

    class Meta:
        db_table = 'reviews_themes'
