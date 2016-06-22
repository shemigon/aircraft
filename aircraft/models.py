from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Aircraft(BaseModel):
    tail_number = models.CharField(max_length=20)
    model_name = models.CharField(max_length=100)
    seat_number = models.PositiveSmallIntegerField()
    manufactured_year = models.PositiveSmallIntegerField()
    insurance_amount = models.FloatField(default=0)
    safety_rating = models.FloatField(blank=True, null=True)
    image_exterior = models.ImageField(blank=True, null=True)
    image_interior = models.ImageField(blank=True, null=True)
    image_floor_plan = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return '{} ({})'.format(self.tail_number, self.model_name)
