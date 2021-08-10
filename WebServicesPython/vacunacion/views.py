from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import transaction
from WebServicesPython.vacunacion.models import *
from WebServicesPython.vacunacion.serializers import *
import json

@api_view(['GET'])
def ciudadano_api_view(request):
    if request.method == 'GET':
        ciudadano = ciudadanos.objects.all()
        ciudadano_serializer = ciudadano_serializer(ciudadano, many = True)
        return Response(ciudadano_serializer.data)

"""
class Vacunacion(APIView):
    def get(self, request, format = None):
        if request.method == 'GET':
            try:
                
                return Response({"historial": "json"})
            except Exception as e:
                return Response({"mensaje": "Sucedió un error al obtener los datos, por favor intente nuevamente."})

    def post(self, request, format = None):
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    json_data = json.loads(request.body.decode('utf-8'))
                    
                    return Response({"mensaje": "La transacción fue realizada correctamente"})    
            except Exception as e: 
                return Response({"mensaje": "Sucedió un error al realizar la transacción, por favor intente nuevamente."})
"""