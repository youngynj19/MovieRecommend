# Generated by Django 3.2.12 on 2022-05-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.IntegerField(),
        ),
    ]
