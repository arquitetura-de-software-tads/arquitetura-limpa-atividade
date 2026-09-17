from abc import ABC, abstractmethod
from entities.Entities import Produto 

class IProdutoDAO(ABC):
    @abstractmethod
    def incluir(self, produto) -> Produto:
        pass
    @abstractmethod
    def alterar(self, produto) -> Produto:
        pass
    @abstractmethod
    def excluir(self, produto):
        pass
    @abstractmethod
    def listar(self):
        pass
    @abstractmethod
    def obter_por_id(self, id):
        pass