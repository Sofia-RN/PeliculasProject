from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, 
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
#models
from .models import Pelicula

#serializer
from .serializers import (
    PeliculaSerializer,
)


# Create your views here.

class PeliculaBuscarApiView(ListAPIView):
        #serializar los datos
    serializer_class = PeliculaSerializer
    
    def get_queryset(self):
        #Filtrar datos
        kword = self.kwargs['kword']
        return Pelicula.objects.filter(
            nombre__icontains=kword
        )



class PeliculaFiltrarApiView(ListAPIView):
        #serializar los datos
    serializer_class = PeliculaSerializer
    
    def get_queryset(self):
        #Filtrar datos
        kword = self.kwargs['kword']
        return Pelicula.objects.filter(
            rango__icontains=kword
        )
        # order_by('apellidos', 'nombre', 'id')