# Generated by Django 3.2.9 on 2022-06-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='norma',
            name='anexo_norma_pdf',
            field=models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Documento del artículo'),
        ),
        migrations.AddField(
            model_name='norma',
            name='anexo_norma_png',
            field=models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Ilustración del artículo'),
        ),
    ]