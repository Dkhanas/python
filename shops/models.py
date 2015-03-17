import email
from django.db import models


class TypeShop(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50, default=None)
    type_shop = models.ForeignKey('TypeShop', default=None)
    owner = models.OneToOneField('contact.Contact', related_name=email, default=None)
    sellers = models.ManyToManyField('contact.Contact',  default=None)
    store = models.ManyToManyField('store.Store', default=None)
    city = models.ForeignKey('place.City', default=None)
    adress = models.CharField(max_length=50, default=None)
    site = models.URLField(blank=True)

    def __unicode__(self):
        return self.name
