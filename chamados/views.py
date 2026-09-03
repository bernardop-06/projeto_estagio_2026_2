from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Chamado
from .forms import ChamadoForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST


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

@login_required
@require_POST
def alterar_status(request, chamado_id):
    chamado = get_object_or_404(Chamado, pk=chamado_id)
    novo_status = request.POST.get("status")

    if novo_status not in dict(Chamado.STATUS):
        messages.error(request, "Status inválido.")
        return redirect("painel")

    chamado.status = novo_status
    chamado.save(update_fields=["status"])
    messages.success(
        request,
        f"Chamado de {chamado.nome} atualizado para {chamado.get_status_display()}.",
    )
    return redirect("painel")    