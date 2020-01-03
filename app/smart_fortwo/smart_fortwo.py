from app.exceptions import CapacidadeMaximaDoSmartFortwoExcedidaException
from app.tripulacao.tripulacao import Tripulacao

_CAPACIDADE_MAXIMA_NO_CARRO = 2

class SmartFortwo:
    def __init__(self):
        self._tripulantes = []

    def adicionar(self, tripulante: Tripulacao) -> None:
        if self.get_quantidade_de_tripulantes() is _CAPACIDADE_MAXIMA_NO_CARRO:
            raise CapacidadeMaximaDoSmartFortwoExcedidaException()
        self._tripulantes.append(tripulante)

    def get_tripulantes(self) -> list:
        return self._tripulantes

    def get_quantidade_de_tripulantes(self) -> int:
        return len(self._tripulantes)










