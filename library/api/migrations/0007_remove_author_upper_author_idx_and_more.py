# Generated by Django 4.0.5 on 2022-07-15 14:23

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_author_upper_author_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='author',
            name='upper_author_idx',
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(django.db.models.expressions.F('name'), name='upper_author_idx'),
        ),
    ]
