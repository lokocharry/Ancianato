# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0008_documento_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='tipo',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'L', b'Licitaci\xc3\xb3n'), (b'D', b'Documento')]),
        ),
    ]
