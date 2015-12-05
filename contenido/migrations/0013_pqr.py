# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0012_auto_20151202_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='PQR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('respuesta', models.TextField()),
            ],
        ),
    ]
