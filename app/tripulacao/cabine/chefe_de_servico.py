from app.tripulacao.tripulacao import Tripulacao


class ChefeDeServico(Tripulacao):
    def __init__(self):
        super().__init__('chefe de serviço')