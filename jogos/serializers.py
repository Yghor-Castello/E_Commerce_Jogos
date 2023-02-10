from rest_framework import serializers
from .models import Produto, Carrinho


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CarrinhoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = Carrinho
        fields = '__all__'