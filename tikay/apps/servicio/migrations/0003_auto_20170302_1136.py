# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20170224_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_solicitud',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='hora_solicitud',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]