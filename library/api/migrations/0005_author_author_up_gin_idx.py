# Generated by Django 4.0.5 on 2022-07-15 14:14

import django.contrib.postgres.indexes
from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_author_options_alter_book_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='author',
            index=django.contrib.postgres.indexes.GinIndex(django.contrib.postgres.indexes.OpClass(django.db.models.functions.text.Upper('name'), name='gin_trgm_ops'), name='author_up_gin_idx'),
        ),
    ]
