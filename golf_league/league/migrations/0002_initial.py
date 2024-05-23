# Generated by Django 4.2.13 on 2024-05-23 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='commissioner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teammanager'),
        ),
        migrations.AddField(
            model_name='league',
            name='current_schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='league.schedule'),
        ),
    ]