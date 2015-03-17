# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('place', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50)),
                ('site', models.URLField(blank=True)),
                ('city', models.ForeignKey(default=None, to='place.City')),
                ('owner', models.OneToOneField(related_name="<module 'email' from 'C:\\Python27\\Lib\\email\\__init__.pyc'>", default=None, to='contact.Contact')),
                ('sellers', models.ManyToManyField(default=None, to='contact.Contact')),
                ('store', models.ManyToManyField(default=None, to='store.Store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeShop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shop',
            name='type_shop',
            field=models.ForeignKey(default=None, to='shops.TypeShop'),
            preserve_default=True,
        ),
    ]
