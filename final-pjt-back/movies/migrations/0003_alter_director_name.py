# Generated by Django 3.2.12 on 2022-05-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]