# Generated by Django 3.2.9 on 2022-06-22 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0004_auto_20220622_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='norma',
            name='fecha',
        ),
        migrations.AddField(
            model_name='norma',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
