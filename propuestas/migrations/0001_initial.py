# Generated by Django 3.2.6 on 2021-08-04 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mantenedores', '0001_initial'),
        ('convencionales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponenteConstitucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componente_constitucion', models.CharField(help_text='Componente Constitucional de Propuesta', max_length=100, unique=True, verbose_name='Componente Constitucional')),
            ],
            options={
                'verbose_name': 'Componente Constitucional',
                'verbose_name_plural': 'Componentes Constitucionales',
            },
        ),
        migrations.CreateModel(
            name='TemaPropuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema_propuesta', models.CharField(help_text='Temas predefinidos de propuestas', max_length=100, unique=True, verbose_name='Tema de Propuesta')),
            ],
            options={
                'verbose_name': 'Tema Propuestas',
                'verbose_name_plural': 'Temas Propuestas',
            },
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problema', models.TextField(blank=True, help_text='¿Cuál es el problema que tú o tu organización busca solucionar?', max_length=225, null=True, verbose_name='Descripción de problema a solucionar')),
                ('situacion', models.TextField(blank=True, help_text='Con respecto al problema planteado, ¿cuál sería la situación ideal?', null=True, verbose_name='Situación ideal de solución')),
                ('componente', models.TextField(blank=True, help_text='Para avanzar en el logro de esa situación ideal, ¿qué debería contemplar la Nueva Constitución?', null=True, verbose_name='Componente de la Constitución')),
                ('otras_organizaciones', models.BooleanField(default=False, help_text='¿Esta propuesta fue elaborada en conjunto con otras organizaciones?', verbose_name='Junto a otras organizaciones')),
                ('organizaciones_de_propuesta', models.TextField(blank=True, help_text="Si tu respuesta fue 'sí', por favor escribe cuáles (separadas por comas). No te olvides de incluir a tu organización.", null=True, verbose_name='Otras Organizaciones')),
                ('compromiso_convencionales', models.BooleanField(default=False, help_text='¿Tu propuesta cuenta con compromisos formales de apoyo de convencionales constituyentes?', verbose_name='Convencionales comprometidos')),
                ('anexo_propuesta', models.FileField(blank=True, help_text='Si has elaborado un documento de tu propuesta en extenso, por favor adjúntalo. Asimismo, si cuentas con otros materiales (estudios, encuestas, presentaciones, material comunicacional, etc.) que complementen tu propuesta, agrégalos.', null=True, upload_to='documents/', verbose_name='Anexos de la Propuesta')),
                ('titulo', models.CharField(help_text='Por favor, revisa el resumen de tu propuesta y escribe un título atractivo para que podamos difundirla hacia la ciudadanía y la Convención Constitucional.', max_length=255, null=True, verbose_name='Título Propuesta')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autor@ de Propuesta')),
                ('comuna', models.ForeignKey(blank=True, help_text='Si la propuesta es comunal, señala la comuna.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comuna_propuesta', to='mantenedores.comuna', verbose_name='Comuna de Propuesta')),
                ('convencionales_comprometidos', models.ManyToManyField(blank=True, help_text="Si tu respuesta fue 'sí', por favor marca todos los/as convencionales que se comprometieron con tu propuesta. Por favor considera que verificaremos esta información.", related_name='convencionales_comprometidos', to='convencionales.Constituyente', verbose_name='Nombres Convencionales Comprometidos')),
                ('otros_temas', models.ManyToManyField(blank=True, help_text='¿Qué otros temas aborda tu propuesta? Por favor selecciona hasta tres temas adicionales.', related_name='otros_temas_propuesta', to='propuestas.TemaPropuesta', verbose_name='Otros Temas de Propuesta')),
                ('region', models.ForeignKey(blank=True, help_text='Si la propuesta es regional, señala la región.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='region_propuesta', to='mantenedores.region', verbose_name='Región de Propuesta')),
                ('tema', models.ForeignKey(help_text='¿Cuál es el tema principal de tu propuesta? Por favor selecciona una categoría del siguiente listado, pues nos ayudará a organizar temáticamente las propuestas en el buscador de la plataforma.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='propuestas.temapropuesta')),
            ],
            options={
                'verbose_name': 'Propuesta Ciudadana',
                'verbose_name_plural': 'Propuestas Ciudadanas',
            },
        ),
    ]