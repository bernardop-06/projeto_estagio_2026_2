from django.db import models


class Chamado(models.Model):
    CATEGORIAS = [
        ("hardware", "Computador não liga/Computador lento"),
        ("software", "Programa não funciona"),
        ("redes", "Problemas com internet/sistema"),
        ("nao_identificada", "Não sei identificar"),
    ]

    STATUS = [
        ("pendente", "Aguardando triagem"),
        ("confirmado", "Em atendimento"),
        ("cancelado", "Cancelado"),
    ]

    nome = models.CharField(max_length=120)
    email = models.EmailField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField(null=True, blank=True)
    descricao = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS, default="pendente")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} — {self.get_categoria_display()}"