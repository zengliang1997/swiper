# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-27 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='权限名称')),
                ('description', models.TextField(verbose_name='权限说明')),
            ],
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='会员名称')),
                ('level', models.IntegerField(default=0, verbose_name='等级')),
                ('price', models.FloatField(verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='VipPermRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vip_id', models.IntegerField()),
                ('perm_id', models.IntegerField()),
            ],
        ),
    ]
