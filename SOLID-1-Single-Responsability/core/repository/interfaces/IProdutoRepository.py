from entities.Entities import Produto

class IProdutoRepository:
    def validar(self, produto):
        pass
    def incluir(self, produto: Produto) -> Produto:
        pass
    def alterar(self, produto: Produto) -> Produto:
        pass
    def excluir(self, produto: Produto):
        pass
    def listar(self):
        pass
    def obter_por_id(self, id):
        pass