# Generated by Django 3.2.9 on 2022-06-23 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0005_auto_20220622_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='norma',
            options={'ordering': ['titulo_web_norma'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.RemoveField(
            model_name='norma',
            name='date_posted',
        ),
    ]
