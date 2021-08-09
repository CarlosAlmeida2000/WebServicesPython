from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from vacunacion import models
import json

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