from django.urls import path
from . import views

urlpatterns = [
    path("", views.pagina_publica, name="pagina_publica"),
    path("enviado/", views.chamado_enviado, name="chamado_enviado"),
]