from django.urls import path
from django.urls.resolvers import URLPattern
from vacunacion import views

urlpatterns = [
    path('consultar-lugar/', views.Vacunacion.as_view()),
]