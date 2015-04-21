# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20150416_1718'),
        ('Noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='tags',
            field=models.ManyToManyField(to='tweets.Tag'),
        ),
    ]
