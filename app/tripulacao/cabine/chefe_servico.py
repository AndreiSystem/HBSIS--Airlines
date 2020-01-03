from app.tripulacao.tripulante import Tripulante


class ChefeServico(Tripulante):
    def __init__(self, nome):
        super().__init__(nome)


start = ChefeServico('piloto')

