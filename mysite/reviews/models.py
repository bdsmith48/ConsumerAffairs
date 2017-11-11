from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    submission_date = models.DateTimeField('date submitted', auto_now=True)
    company = models.CharField(max_length=30)
    reviewer_name = models.CharField(max_length=30)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]) 

