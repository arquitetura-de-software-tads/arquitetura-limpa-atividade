from dao.interfaces.IConexaoDB import IConexaoDB
from sqlite3 import connect

class ConexaoDB(IConexaoDB):
    def obter_conexao(self):
        conexao = connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;")
    
    def executar_comando(self, sql_comando):
        conexao = ConexaoDB.obter_conexao()
        conexao.cursor().execute(sql_comando)
        conexao.commit()

    def executar_select(self, sql_select):
        conexao = ConexaoDB.obter_conexao()
        registros = conexao.cursor().execute(sql_select).fetchall()
        return registros