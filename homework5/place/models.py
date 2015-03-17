from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', default=None)

    def __unicode__(self):
        return self.name