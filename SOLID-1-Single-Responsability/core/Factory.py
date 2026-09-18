from dao.CategoriaDAO import CategoriaDAO
from dao.ProdutoDAO import ProdutoDAO
from dao.ConexaoDB import ConexaoDB 
from repository.CategoriaRepository import CategoriaRepository
from repository.ProdutoRepository import ProdutoRepository

class Factory:
    @staticmethod
    def obter_conexao_db():
        return ConexaoDB()

    @staticmethod
    def obter_produto_dao():
        return ProdutoDAO(Factory.obter_conexao_db())

    @staticmethod
    def obter_categoria_dao():
        return CategoriaDAO(Factory.obter_conexao_db())

    @staticmethod
    def obter_categoria_repository():
        return CategoriaRepository(Factory.obter_categoria_dao())
    
    @staticmethod
    def obter_produto_repository():
        return ProdutoRepository(Factory.obter_produto_dao())