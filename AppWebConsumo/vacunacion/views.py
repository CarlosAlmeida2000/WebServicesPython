from django.shortcuts import render
from .service import get_LgVotac
# Create your views here.

def vwLugarVotac(request):
    context = {
        'historial': get_LgVotac()
    }
    return render(request,'index.html',context)
