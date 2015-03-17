from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50)
    sitys = models.ForeignKey('place.City')
    adress = models.CharField(max_length=50, default=None)

    def __unicode__(self):
        return self.name
