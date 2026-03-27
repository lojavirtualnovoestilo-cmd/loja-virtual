from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(verbose_name="Descrição")
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Venda (R$)")
    imagem_url = models.URLField(verbose_name="Link da Imagem (do fornecedor)")
    link_pagamento = models.URLField(verbose_name="Link do Stripe (Checkout)")
    estoque = models.IntegerField(default=10)

    def __str__(self):
        return self.nome
