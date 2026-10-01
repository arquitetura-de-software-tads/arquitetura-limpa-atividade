from core.entities.demanda import Demanda
from ports.idao.idemanda import IDemandaDAO

class DemandaRepository:
    def __init__(self, dao: IDemandaDAO) -> None:
        self.dao = dao

    def validar(self, demanda: Demanda):
        if DemandaRepository.obter_por_id(demanda.id) is None:
            raise ValueError("Não existe demanda com esse id")
        if (demanda.exigencias.strip() == "") or (not demanda.exigencias):
            raise ValueError("Exigência é obrigatória")
        if (demanda.prazo.strip() == "") or (not demanda.prazo):
            raise ValueError("Prazo é obrigatório")      

    def incluir(self, demanda: Demanda) -> Demanda:
        self.validar(demanda)
        obj = self.dao.incluir(demanda)
        return obj

    def alterar(self, demanda: Demanda) -> Demanda:
        self.validar(demanda)
        obj = self.dao.alterar(demanda)
        return obj

    def excluir(self, demanda: Demanda) -> None:
        self.validar(demanda)
        self.dao.excluir(demanda)

    def listar(self) -> list[Demanda]:
        return self.dao.listar()

    def obter_por_id(self, id: int) -> Demanda:
        return self.dao.obter_por_id(id)