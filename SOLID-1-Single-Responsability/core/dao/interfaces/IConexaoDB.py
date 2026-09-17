from abc import ABC

class IConexaoDB(ABC):
    def obter_conexao(self):
        pass
    def executar_comando(self, sql_comando):
        pass
    def executar_select(self, sql_select):
        pass