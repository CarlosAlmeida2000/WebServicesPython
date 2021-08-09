from django.shortcuts import render
from .service import get_LgVacun
# Create your views here.

def vwLugarVacun(request):
    context = {
        'historial': get_LgVacun()
    }
    return render(request,'index.html',context)
