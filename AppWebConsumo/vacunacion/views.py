from django.shortcuts import render
from .service import get_LgVacun

# Create your views here.


def vwLugarVacun(request):
    return render(request, "index.html")
