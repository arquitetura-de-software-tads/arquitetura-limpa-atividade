from dao.interfaces.IProdutoDAO import IProdutoDAO
from core.Factory import Factory
from entities.Entities import Produto
from repository.interfaces.IProdutoRepository import IProdutoRepository

class ProdutoRepository(IProdutoRepository):
    def __init__(self, dao: IProdutoDAO):
        self.dao = dao

    # tô usando pra validar o objeto e se retornar false, bloqueia a operação
    def validar(self, produto: Produto) -> Produto:
        if produto is None:
            return False
        if produto[1] == "": # descrição
            return False
        if produto[2] == "" or produto[2] < 0: # preço unitário
            return False
        if produto[3] == "" or produto[3] < 0: # estoque
            return False
        if produto[4] is None: # id da categoria
            return False
        else:
            dao = Factory.obter_categoria_dao()
            categoria = dao.obter_por_id(produto[4])
            if categoria is None: 
                return False
        return True
         
    def incluir(self, produto: Produto) -> Produto:
        validacao = self.validar(produto)
        if validacao:
            dao = Factory.obter_produto_dao()
            dao.incluir(produto)
            return produto
        return None

    def alterar(self, produto: Produto) -> Produto:
        validacao = self.validar(produto)
        if validacao:
            dao = Factory.obter_produto_dao()
            dao.alterar(produto)
            return produto
        return None

    def excluir(self, produto: Produto):
        validacao = self.validar(produto)
        if validacao:
            dao = Factory.obter_produto_dao()
            dao.excluir(produto)
        return None

    def listar(self):
        dao = Factory.obter_produto_dao()
        return dao.listar()

    def obter_por_id(self, id: int) -> Produto:
        if id is None:
            return None
        dao = Factory.obter_produto_dao()
        produto = dao.obter_por_id(id)
        return produto