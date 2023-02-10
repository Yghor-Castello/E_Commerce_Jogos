from django.contrib import admin
from .models import Produto, Carrinho, CarrinhoProduto


admin.site.register(Produto)
admin.site.register(CarrinhoProduto)
admin.site.register(Carrinho)
