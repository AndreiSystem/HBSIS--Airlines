from app.tripulacao.tripulacao import Tripulacao


class Oficial(Tripulacao):
    def __init__(self):
        super().__init__('oficial')