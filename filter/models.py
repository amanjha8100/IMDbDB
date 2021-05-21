from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Directors(models.Model):
    name = models.TextField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directors'
        


class Movies(models.Model):
    original_title = models.CharField(max_length=500,blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    director_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movies'

class Movie(models.Model):
    director = models.ForeignKey(Directors,on_delete=CASCADE,null=True)
    original_title = models.CharField(max_length=500,blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    # director_id = models.IntegerField()