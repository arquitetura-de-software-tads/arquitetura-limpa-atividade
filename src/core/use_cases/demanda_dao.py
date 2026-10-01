from core.entities.demanda import Demanda
from ports.idao.idemanda import IDemandaDAO

# DAO fake
class DemandaDAO(IDemandaDAO):
    def incluir(self, demanda: Demanda) -> Demanda:
        return Demanda(demanda.id, demanda.exigencias, demanda.prazo)
    def alterar(self, demanda: Demanda) -> Demanda:
        return Demanda(demanda.id, demanda.exigencias, demanda.prazo)