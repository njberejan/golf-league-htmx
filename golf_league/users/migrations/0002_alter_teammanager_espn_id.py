# Generated by Django 4.2.13 on 2024-05-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammanager',
            name='espn_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
