from django import forms
from django.db import transaction
from django.forms import ModelForm
from propuestas.models import Propuesta, TemaPropuesta
from mantenedores.models import *



class PropuestaForm1(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'pais',
        'region',
        'comuna'
        ]
        labels = {
            'pais': ('<h6><span style="text-transform:uppercase">1. País</span></h6><i>Selecciona tu país</i>'),
            'region': ('<h6><span style="text-transform:uppercase">2. Región</span></h6><i>Selecciona tu región</i>'),
            'comuna': ('<h6><span style="text-transform:uppercase">3. Comuna</span></h6><i>Selecciona tu comuna</i>'),
        }



class PropuestaForm2(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'tema',
        'otros_temas',
        'tema_extra',
        ]
        labels = {
            'tema': ('<h6><span style="text-transform:uppercase">1. ¿Cuál es el tema principal de tu propuesta?</span></h6><i>Selecciona tema principal</i>'),
            'otros_temas': ('<h6><span style="text-transform:uppercase">2. ¿Qué otros temas aborda tu propuesta?</span></h6><i>Por favor selecciona hasta tres temas adicionales</i>'),
            'tema_extra': ('<h6><span style="text-transform:uppercase">3. Otro tema, ¿cuál?</span></h6><i>Si tu propuesta contempla algún tema que no está en el listado, por favor escríbelo aquí en una palabra o frase breve</i>'),
        }



class PropuestaForm3(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'problema',
        'situacion',
        'componente'
        ]
        labels = {
            'problema': ('<h6><span style="text-transform:uppercase">1. ¿Cuál es el problema que tú o tu organización busca solucionar?</span></h6><i>Ejemplo: El actual sistema de seguridad social no garantiza pensiones dignas para todas las personas.</i>'),
            'situacion': ('<h6><span style="text-transform:uppercase">2. Con respecto al problema planteado, ¿cuál sería la situación ideal?</span></h6><i>Ejemplo: Cuando jubilan, todas las personas tienen acceso a una pensión que cubre sus necesidades básicas para vivir con dignidad.</i>'),
            'componente': ('<h6><span style="text-transform:uppercase">3. Para avanzar en el logro de esa situación ideal, ¿qué debería contemplar la Nueva Constitución?</span></h6><i>Ejemplo: Consagrar constitucionalmente el derecho a la protección social y explicitar la obligación del Estado de asegurar a todas las personas una pensión digna.</i>'),
        }
        widgets = {
            'problema': forms.Textarea(attrs={'placeholder': 'Describe el problema de manera precisa y breve en un máximo de 250 palabras.'}),
            'situacion': forms.Textarea(attrs={'placeholder': 'Describe la situación ideal de manera precisa y breve en un máximo de 250 palabras.'}),
            'componente': forms.Textarea(attrs={'placeholder': 'Escribe tu propuesta de manera precisa y breve en un máximo de 250 palabras.'}),
        }



class PropuestaForm4(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'otras_organizaciones',
        'organizaciones_de_propuesta'
        ]
        widgets = {
            'otras_organizaciones': forms.CheckboxInput()
        }
        labels = {
            'otras_organizaciones': ('<h6><span style="text-transform:uppercase">1. ¿Esta propuesta fue elaborada en conjunto con otras organizaciones?</span></h6><i>Marque si es así.</i>'),
            'organizaciones_de_propuesta': ('<h6><span style="text-transform:uppercase">2. Si tu respuesta fue “sí”, escribe cuáles:</span></h6><i>Por favor escribe los nombres de las organizaciones que participaron en la elaboración de la propuesta. No olvides mencionar a tu organización.</i>'),
        }



class PropuestaForm5(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'compromiso_convencionales',
        'anexo3_propuesta',
        ]
        widgets = {
            'compromiso_convencionales': forms.CheckboxInput()
        }
        labels = {
            'compromiso_convencionales': ('<h6><span style="text-transform:uppercase">1. ¿Tu propuesta cuenta con compromisos formales de apoyo de convencionales constituyentes?</span></h6><i>Marque si es así.</i>'),
            'anexo3_propuesta': ('<i>Si tienes un documento o archivo que acredite los compromisos, ingrésalo acá.</i>'),

        }



class PropuestaForm6(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'anexo_propuesta',
        'anexo2_propuesta',
        'link_extra1',
        'link_extra2'
        ]
        labels = {
            'anexo_propuesta': ('<h6><span style="text-transform:uppercase">Si has elaborado un documento con tu propuesta constitucional desarrollada en mayor detalle y profundidad, adjúntalo:</span></h6>'),
            'anexo2_propuesta': ('<i>Asimismo, si cuentas con otros materiales (estudios, encuestas, presentaciones, material comunicacional, etc.) que complementen tu propuesta, agrégalos.</i>'),
            'link_extra1': ('<i>Link a material complementario.</i>'),
            'link_extra2': ('<i>Otro link a material complementario.</i>'),
        }



class PropuestaForm7(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'titulo'
        ]
        labels = {
            'titulo': ('<h6><span style="text-transform:uppercase">Escribe un título atractivo para que podamos difundirla entre la ciudadanía y en la Convención Constitucional.</span></h6><i>Título: máximo 280 caracteres</i>'),
        }



# class CrearPropuestaForm(forms.ModelForm):
#     class Meta:
#         model = Propuesta
#         fields = [
#         'pais',
#         'region',
#         'comuna',
#         'tema',
#         'otros_temas',
#         'problema',
#         'situacion',
#         'componente',
#         'otras_organizaciones',
#         'organizaciones_de_propuesta',
#         'compromiso_convencionales',
#         'convencionales_comprometidos',
#         'anexo_propuesta',
#         'titulo'
#         ]
