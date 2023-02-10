from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    score = models.FloatField()
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome

class CarrinhoProduto(models.Model):
    carrinho = models.ForeignKey('Carrinho', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.produto.preco * self.quantidade
    
    def __str__(self):
        return self.carrinho

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='CarrinhoProduto')

    def __str__(self):
        return f"Carrinho de compras de {self.usuario}"

    def subtotal(self):
        return sum(item.subtotal() for item in self.carrinhoproduto_set.all())

    def frete(self):
        subtotal = self.subtotal()
        if subtotal >= 250:
            return 0
        else:
            return 10.0

    def total(self):
        return self.subtotal() + self.frete()