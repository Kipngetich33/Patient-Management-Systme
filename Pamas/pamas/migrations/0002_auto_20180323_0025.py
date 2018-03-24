# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 21:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pamas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='hospital',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]