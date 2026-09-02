from django import forms
from django.utils import timezone

from .models import Chamado


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ["nome", "email", "categoria", "data_inicio", "hora_inicio", "descricao"]
        labels = {
            "nome": "Seu nome",
            "email": "Seu e-mail",
            "categoria": "O que está acontecendo?",
            "data_inicio": "Quando o problema começou?",
            "hora_inicio": "Por volta de que horas? (se souber)",
            "descricao": "Conte o que aconteceu",
        }
        widgets = {
            "data_inicio": forms.DateInput(attrs={"type": "date"}),
            "hora_inicio": forms.TimeInput(attrs={"type": "time"}),
            "descricao": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].choices = [
            ("", "Escolha a opção mais parecida"),
        ] + Chamado.CATEGORIAS
        for campo in self.fields.values():
            campo.widget.attrs.setdefault(
                "class", "w-full rounded-lg border border-slate-300 px-3 py-2"
            )

    def clean_data_inicio(self):
        data = self.cleaned_data["data_inicio"]
        if data > timezone.localdate():
            raise forms.ValidationError("O problema não pode ter começado no futuro.")
        return data