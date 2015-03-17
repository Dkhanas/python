# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(default=None, max_length=50)),
                ('sitys', models.ForeignKey(to='place.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
