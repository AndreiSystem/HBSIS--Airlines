from abc import ABC

class Tripulante(ABC):
    def __init__(self, nome: str):
        self._nome = nome
        self._tripulacao = []

    def get_nome(self):
        return self._nome




