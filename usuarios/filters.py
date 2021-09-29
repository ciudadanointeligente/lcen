import django_filters
from django_filters import filters
from .models import User, Convencional
from mantenedores.models import *
from convencionales.models import *


class ConvencionalesFiltro(django_filters.FilterSet):

    lista = filters.ModelChoiceFilter(queryset=Lista.objects.all().distinct(), label='', empty_label='Buscar por Colectivo...')
    distrito = filters.ModelChoiceFilter(queryset=Distrito.objects.all().distinct(), label='', empty_label='Buscar por Distrito...')
    movimiento = filters.ModelChoiceFilter(queryset=Movimiento.objects.all().distinct(), label='', empty_label='Buscar por Partido/Movimiento...')



    class Meta:
        model = Convencional
        fields = ('lista','distrito','movimiento',)
