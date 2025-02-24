# Generated by Django 4.0.5 on 2022-07-03 21:17

from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        TrigramExtension(),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('edition', models.PositiveIntegerField(max_length=5)),
                ('publication_year', models.PositiveIntegerField(max_length=4)),
                ('authors', models.ManyToManyField(related_name='books', through='api.BookAuthor', to='api.author')),
            ],
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.books'),
        ),
    ]
