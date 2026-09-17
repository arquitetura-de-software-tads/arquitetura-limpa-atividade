from dao.interfaces.IConexaoDB import IConexaoDB
from dao.interfaces.IProdutoDAO import IProdutoDAO
from dao.ConexaoDB import ConexaoDB 
from entities.Entities import Produto

class ProdutoDAO(IProdutoDAO):
    def __init__(self, conexao: IConexaoDB):
        self.conexao = conexao

    def incluir(self, produto: Produto) -> Produto:
        comando = f"INSERT INTO Produto(descricao, preco_unitario, quantidade_estoque, categoria_id) VALUES({produto[1], produto[2], produto[3], produto[4]})"
        ConexaoDB.executar_comando(comando, True)
        return produto

    def alterar(self, produto: Produto) -> Produto:
        comando = f"UPDATE Produto SET descricao = {produto[1]}, preco_unitario = {produto[2]}, quantidade_estoque = {produto[3]}, categoria_id = {produto[4]} WHERE id = {produto[0]}"
        ConexaoDB.executar_comando(comando)
        return produto

    def excluir(self, produto: Produto) -> None:
        comando = f"DELETE FROM Produto WHERE id = {produto[0]}"
        ConexaoDB.executar_comando(comando)

    def listar(self):
        comando = f"SELECT pro.id, pro.descricao, pro.preco_unitario, pro.quantidade_estoque, pro.categoria_id, cat.descricao as categoria FROM Produto pro INNER JOIN Categoria cat ON cat.id = pro.categoria_id ORDER BY pro.descricao"
        registros = ConexaoDB.executar_select(comando)
        return registros

    def obter_por_id(self, id):
        comando = f"SELECT id, descricao, preco_unitario, quantidade_estoque, categoria_id FROM Produto WHERE id={id}"
        registro = ConexaoDB.executar_select(comando)
        produto = Produto(id, registro[1], registro[2], registro[3], registro[4])
        return produto