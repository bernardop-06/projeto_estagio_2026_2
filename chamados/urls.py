from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.pagina_publica, name="pagina_publica"),
    path("enviado/", views.chamado_enviado, name="chamado_enviado"),
    path("painel/", views.painel, name="painel"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="chamados/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("painel/<int:chamado_id>/status/", views.alterar_status, name="alterar_status"),
]