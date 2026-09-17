from dao.interfaces.IConexaoDB import IConexaoDB
from dao.interfaces.IProdutoDAO import IProdutoDAO
from entities.Entities import Produto

class ProdutoDAO(IProdutoDAO):
    def __init__(self, conexao: IConexaoDB):
        self.conexao = conexao

    