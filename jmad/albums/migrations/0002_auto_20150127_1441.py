# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_number',
            field=models.PositiveIntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
