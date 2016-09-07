# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-06 22:18
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bars', '0001_initial'),
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('photos', models.ImageField(upload_to='/media/images')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('bandas', models.ManyToManyField(to='bands.Band')),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bars.Bar')),
            ],
        ),
    ]