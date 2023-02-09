from rest_framework.routers import SimpleRouter

from .views import ListProdutosView, DetailProdutoView, ListCarrinhoView, DetailCarrinhoView


router = SimpleRouter()
router.register('produtos', ListProdutosView)
router.register('detalhesproduto', DetailProdutoView)
router.register('carrinho', ListCarrinhoView)
router.register('detalhescarrinho', DetailCarrinhoView)

