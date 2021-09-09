from django.shortcuts import render
from django.http import HttpResponse
from propuestas.models import Propuesta
from django.views.generic import TemplateView
from django.db.models import Count



class LandingView(TemplateView):
    template_name = 'inicio/presentacion.html'



class EsperaView(TemplateView):
    template_name = 'inicio/en_construccion.html'



class HomeView(TemplateView):
    template_name = 'inicio/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['propuestas'] = Propuesta.objects.annotate(apoyos_count=Count('apoyos')).order_by('-autor__organizacion','-apoyos_count')[:3]
        return context



class QueesView(TemplateView):
    template_name = 'inicio/que_es.html'



class PreguntasView(TemplateView):
    template_name = 'inicio/preguntas-frecuentes.html'



class TerminosView(TemplateView):
    template_name = 'inicio/terminos.html'
