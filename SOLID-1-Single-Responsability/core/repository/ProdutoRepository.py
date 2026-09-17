from dao.interfaces.IProdutoDAO import IProdutoDAO
from entities.Entities import Produto
from repository.interfaces.IProdutoRepository import IProdutoRepository

class ProdutoRepository(IProdutoRepository):
    def __init__(self, dao: IProdutoDAO):
        self.dao = dao

    def validar(self, produto: Produto) -> Produto:
        # as validacoes vao ser as mesmas para todos os seguintes metodos,
        # entao é mais facil socar tudo aqui
        if produto is None:
            raise Exception("O produto não pode ser nulo")
         
    def incluir(self, produto: Produto) -> Produto:
        pass