# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='adress',
            field=models.CharField(default=None, max_length=50),
            preserve_default=True,
        ),
    ]
