from dataclasses import dataclass

@dataclass
class Categoria:
    id: int
    descricao: str

    def __init__(self, id: int, descricao: str):
        self.id = id
        self.descricao = descricao

@dataclass
class Produto:
    id: int
    descricao: str
    preco_unitario: float
    quantidade_estoque: int
    categoria: Categoria

    def __init__(self, id: int, descricao: str, preco_unitario: float, quantidade_estoque: int, categoria: Categoria):
        self.id = id
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria