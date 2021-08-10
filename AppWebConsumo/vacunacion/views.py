from django.shortcuts import render
from .service import get_LgVacun# método que obtiene los datos
# Create your views here.

def vwLugarVacun(request):
    if request.method == 'POST':
        cedula=request.POST["cedula"]
        nombres=request.POST["nombres"]
        params = { 
                    'cedula': cedula,
                    'nombres': nombres
                 }
        context = {
            'result': get_LgVacun(params)
        }
        return render(request, "index.html",context)
    return render(request, "index.html")
