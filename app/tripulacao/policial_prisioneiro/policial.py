from app.tripulacao.tripulacao import Tripulacao


class Policial(Tripulacao):
    def __init__(self):
        super().__init__('policial')