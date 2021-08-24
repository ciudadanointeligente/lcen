from django.urls import path
from . import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('ciudadano_register/',views.ciudadano_register.as_view(), name='ciudadano_register'),
     path('organizacion_register/',views.organizacion_register.as_view(), name='organizacion_register'),
     path('organizacion_update/',views.organizacion_update.as_view(), name='organizacion_update'),
     path('verorganizaciones/',views.VerOrganizacionesView.as_view(), name='verorganizaciones'),
     path('verorganizaciones/<pk>',views.VerOrganizacionView.as_view(), name='verorganizacion'),
     path('convencional_register/',views.convencional_register.as_view(), name='convencional_register'),
     path('verconvencionales/',views.VerConvencionalesView.as_view(), name='verconvencionales'),
     path('verconvencionales/<pk>',views.VerConvencionalView.as_view(), name='verconvencional'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]
