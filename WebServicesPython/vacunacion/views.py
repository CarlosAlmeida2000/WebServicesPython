from typing import ContextManager
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import transaction
from vacunacion.models import *   
from vacunacion.serializers import *
import json

'''
@api_view(['GET'])
def ciudadano_api_view(request):
    if request.method == 'GET':
        ciudadano = ciudadanos.objects.all()
        ciudadano_serializer = ciudadano_serializer(ciudadano, many = True)
        return Response(ciudadano_serializer.data)
'''

class Vacunacion(APIView):
    
    def post(self, request, format = None):
        if request.method == 'POST':
            try:
                json_data = json.loads(request.body.decode('utf-8'))
                cedula = json_data[0]['cedula']
                nombres = (json_data[0]['nombres']).split()
                nombre1 = nombres[0].upper()
                nombre2 = nombres[1]
                apellido1 = nombres[2]
                apellido2 = nombres[3]
                unCiudadano = ciudadanos.objects.get(cedula=cedula, nombre1__icontains=nombre1, nombre2__icontains=nombre2, apellido1__icontains=apellido1, apellido2__icontains=apellido2)
                json_consulta = {
                    "nombres": json_data[0]['nombres'].upper(),
                    "provincia": unCiudadano.provincia.provincia,
                    "canton": unCiudadano.canton.canton,
                    "centro_vacunacion": unCiudadano.centroVacunacion.centro_vacunacion,
                    "direccion": unCiudadano.centroVacunacion.direccion,
                    "primera_dosis": unCiudadano.primeraDosis,
                    "segunda_dosis": unCiudadano.segundaDosis
                }
                return Response({"consulta": json_consulta})    
            except ciudadanos.DoesNotExist:
                return Response({"mensaje": "Ups, no se encuentra registrado...."})
