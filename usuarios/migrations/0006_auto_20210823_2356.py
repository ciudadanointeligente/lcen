# Generated by Django 3.2.6 on 2021-08-24 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedores', '0001_initial'),
        ('convencionales', '0001_initial'),
        ('usuarios', '0005_organizacion_nombre_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='convencional',
            name='biografia',
            field=models.TextField(blank=True, null=True, verbose_name='Historia Política'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='cargo',
            field=models.ManyToManyField(blank=True, related_name='cargos_en_constituyente', to='convencionales.Cargo', verbose_name='Cargos de Constituyente en la Convención'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distrito_de_constituyente', to='mantenedores.distrito', verbose_name='Distrito del Constituyente'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='facebook',
            field=models.URLField(blank=True, max_length=254, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_constituyentes/', verbose_name='Foto Constituyente'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='instagram',
            field=models.URLField(blank=True, max_length=254, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='linkintereses',
            field=models.URLField(blank=True, max_length=225, null=True, verbose_name='Link Declaración de Intereses'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='lista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lista_de_constituyente', to='convencionales.lista', verbose_name='Lista del Constituyente'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='movimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimiento_de_constituyente', to='convencionales.movimiento', verbose_name='Partido/Movimiento del Constituyente'),
        ),
        migrations.AddField(
            model_name='convencional',
            name='twitter',
            field=models.URLField(blank=True, max_length=254, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='convencional',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail de Contacto'),
        ),
    ]