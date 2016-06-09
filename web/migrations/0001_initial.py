# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ip', models.CharField(db_index=True, max_length=15)),
                ('todayLoginTimes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='signLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script', models.CharField(max_length=255)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.BinaryField()),
                ('registTime', models.DateTimeField()),
                ('registIp', models.CharField(max_length=15, null=True)),
                ('loginTimes', models.IntegerField(default=0)),
                ('lastLoginIp', models.CharField(max_length=15, null=True)),
                ('lastLoginTime', models.DateTimeField()),
                ('ban', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='signlog',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.user', to_field='email'),
        ),
    ]
