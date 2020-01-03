from app.tripulacao.tripulacao import Tripulacao


class Prisioneiro(Tripulacao):
    def __init__(self):
        super().__init__('prisioneiro')