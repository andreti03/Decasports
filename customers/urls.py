from django.urls import path
from .views import index, formulario

urlpatterns = [
    path('', index, name = 'profile'),
    #path('customers/encuesta.html', formulario)
]