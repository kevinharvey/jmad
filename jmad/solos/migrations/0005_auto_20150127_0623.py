# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('solos', '0004_solo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solo',
            name='album',
        ),
        migrations.AlterField(
            model_name='solo',
            name='track',
            field=models.ForeignKey(to='albums.Track'),
            preserve_default=True,
        ),
    ]
