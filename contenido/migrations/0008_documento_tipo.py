# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0007_historia'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='tipo',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
    ]
