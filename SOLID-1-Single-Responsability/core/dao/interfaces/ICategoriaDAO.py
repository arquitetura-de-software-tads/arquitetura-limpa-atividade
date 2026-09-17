from abc import ABC, abstractmethod
from app.dao.interfaces import IDAO 

class ICategoriaDAO(ABC):
    @abstractmethod
    def incluir(self, categoria):
        pass
    @abstractmethod
    def alterar(self, categoria):
        pass
    @abstractmethod
    def excluir(self, categoria):
        pass
    @abstractmethod
    def obter_por_id(self, id):
        pass
    @abstractmethod
    def listar(self):
        pass