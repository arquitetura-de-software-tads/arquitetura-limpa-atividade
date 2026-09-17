from dao.interfaces.IConexaoDB import IConexaoDB
from dao.interfaces.ICategoriaDAO import ICategoriaDAO
from dao.ConexaoDB import ConexaoDB 
from entities.Entities import Categoria

class CategoriaDAO(ICategoriaDAO):
    def __init__(self, conexao: IConexaoDB):
        self.conexao = conexao

    def incluir(self, categoria: Categoria) -> Categoria:
        comando = f"INSERT INTO Categoria(descricao) VALUES({categoria[1]})"
        ConexaoDB.executar_comando(comando, True)
        return categoria

    def alterar(self, categoria: Categoria) -> Categoria:
        comando = f"UPDATE Categoria SET descricao = {categoria[1]} WHERE id = {categoria[0]}"
        ConexaoDB.executar_comando(comando)
        return categoria

    def excluir(self, categoria: Categoria) -> None:
        comando = f"DELETE FROM Categoria WHERE id = {categoria[0]}"
        ConexaoDB.executar_comando(comando)

    def listar(self):
        comando = f"SELECT cat.id, cat.descricao FROM Categoria ORDER BY pro.descricao"
        registros = ConexaoDB.executar_select(comando)
        return registros

    def obter_por_id(self, id):
        comando = f"SELECT id, descricao FROM Categoria WHERE id={id}"
        registro = ConexaoDB.executar_select(comando)
        categoria = Categoria(id, registro[1])
        return categoria