from app.tripulacao.policial_prisioneiro.policial import Policial
from app.tripulacao.policial_prisioneiro.prisioneiro import Prisioneiro
from app.tripulacao.tecnica.piloto import Piloto
from app.tripulacao.tecnica.oficial import Oficial
from app.tripulacao.cabine.chefe_de_servico import ChefeDeServico
from app.tripulacao.cabine.comissaria import Comissaria

class Terminal:
    def __init__(self):

        self._terminal = [
            Piloto(),
            ChefeDeServico(),
            Policial(),
            Oficial(),
            Oficial(),
            Comissaria(),
            Comissaria(),
            Prisioneiro()
        ]

    def get_tripulantes(self):
        return self._terminal






