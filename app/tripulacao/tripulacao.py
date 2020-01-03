from abc import ABC

class Tripulacao(ABC):
    def __init__(self, nome : str):
        self._nome = nome

    def __str__(self):
        return self._nome