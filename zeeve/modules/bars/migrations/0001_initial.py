# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-06 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_foundation', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('work_time', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='', verbose_name='/image/logo')),
            ],
        ),
    ]