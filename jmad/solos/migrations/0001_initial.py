# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('instrument', models.CharField(max_length=200)),
                ('start_time', models.CharField(max_length=20, null=True, blank=True)),
                ('end_time', models.CharField(max_length=20, null=True, blank=True)),
                ('slug', models.SlugField()),
                ('track', models.ForeignKey(to='albums.Track')),
            ],
            options={
                'ordering': ['track', 'start_time'],
            },
        ),
    ]
