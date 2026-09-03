from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Chamado
from .forms import ChamadoForm


def pagina_publica(request):
    if request.method == "POST":
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("chamado_enviado")
    else:
        form = ChamadoForm()

    return render(request, "chamados/publica.html", {"form": form})


def chamado_enviado(request):
    return render(request, "chamados/enviado.html")

@login_required
def painel(request):
    chamados = Chamado.objects.order_by("data_inicio", "hora_inicio")
    return render(request, "chamados/painel.html", {"chamados": chamados})