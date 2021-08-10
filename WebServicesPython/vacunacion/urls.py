from django.urls import path
from django.urls.resolvers import URLPattern
from WebServicesPython.vacunacion import views

urlpatterns = [
    path('consultar-lugar/', views.ciudadano_api_view),
]