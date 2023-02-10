from rest_framework import viewsets
from .models import Produto, Carrinho
from .serializers import ProdutoSerializer, CarrinhoSerializer

class ListProdutosView(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def get_queryset(self):
        queryset = Produto.objects.all()
        sort = self.request.query_params.get("sort", None)
        if sort == "price":
            queryset = queryset.order_by("price")
        elif sort == "popularity":
            queryset = queryset.order_by("-popularity")
        elif sort == "alphabetical":
            queryset = queryset.order_by("name")

        return queryset

class DetailProdutoView(viewsets.ReadOnlyModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListCarrinhoView(viewsets.ReadOnlyModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

    def get_queryset(self):
        queryset = Carrinho.objects.all()
        usuario = self.request.query_params.get("usuario", None)
        if usuario:
            queryset = queryset.filter(usuario=usuario)

        return queryset

class DetailCarrinhoView(viewsets.ReadOnlyModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

