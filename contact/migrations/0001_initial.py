# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('sex', models.CharField(default=b'3', max_length=6, choices=[(b'1', b'man'), (b'2', b'woman'), (b'3', b'-----')])),
                ('birthday', models.DateField(default=None, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=75, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
