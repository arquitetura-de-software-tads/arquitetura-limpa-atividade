from entities.Entities import Categoria

class ICategoriaRepository:
    def validar(self, categoria):
        pass
    def incluir(self, categoria: Categoria) -> Categoria:
        pass
    def alterar(self, categoria: Categoria) -> Categoria:
        pass
    def excluir(self, categoria: Categoria):
        pass
    def listar(self):
        pass
    def obter_por_id(self, id):
        pass