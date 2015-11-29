# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_mision_vision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mision',
            old_name='contenido',
            new_name='mision',
        ),
        migrations.RenameField(
            model_name='vision',
            old_name='contenido',
            new_name='vision',
        ),
    ]
