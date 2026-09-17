from dao.interfaces.ICategoriaDAO import ICategoriaDAO
from dao.interfaces.IProdutoDAO import IProdutoDAO
from dao.CategoriaDAO import CategoriaDAO
from dao.ProdutoDAO import ProdutoDAO 
from dao.ConexaoDB import ConexaoDB 

class Factory():
    def obter_conexao_db(self):
        return ConexaoDB()
    
    def obter_produto(self):
        return ProdutoDAO(self.obter_conexao_db())