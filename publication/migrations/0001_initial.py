# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 15:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Publications',
            },
        ),
    ]
