from dao.interfaces.ICategoriaDAO import ICategoriaDAO
from core.Factory import Factory
from entities.Entities import Categoria
from repository.interfaces.ICategoriaRepository import ICategoriaRepository

class CategoriaRepository(ICategoriaRepository):
    def __init__(self, dao: ICategoriaDAO):
        self.dao = dao

    # tô usando pra validar o objeto e se retornar false, bloqueia a operação
    def validar(self, categoria: Categoria) -> Categoria:
        if categoria is None:
            return False
        if categoria[1] == "": # descrição
            return False
        return True
         
    def incluir(self, categoria: Categoria) -> Categoria:
        validacao = self.validar(categoria)
        if validacao:
            dao = Factory.obter_categoria_dao()
            dao.incluir(categoria)
            return categoria
        return None

    def alterar(self, categoria: Categoria) -> Categoria:
        validacao = self.validar(categoria)
        if validacao:
            dao = Factory.obter_categoria_dao()
            dao.alterar(categoria)
            return categoria
        return None

    def excluir(self, categoria: Categoria):
        validacao = self.validar(categoria)
        if validacao:
            dao = Factory.obter_categoria_dao()
            dao.excluir(categoria)
        return None

    def listar(self):
        dao = Factory.obter_categoria_dao()
        return dao.listar()

    def obter_por_id(self, id: int) -> Categoria:
        if id is None:
            return None
        dao = Factory.obter_categoria_dao()
        categoria = dao.obter_por_id(id)
        return categoria