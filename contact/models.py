from django.db import models


class Contact(models.Model):
    SEX_CHOISES = (
        ('1', 'man'),
        ('2', 'woman'),
        ('3', '-----')
    )
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    sex = models.CharField(default='3', max_length=6, choices=SEX_CHOISES)
    birthday = models.DateField(default=None, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)


    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.second_name)
