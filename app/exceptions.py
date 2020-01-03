class CapacidadeMaximaDoSmartFortwoExcedidaException(Exception):
    def __init__(self, msg: str = 'Capacidade maxima do smart fortwo excedida'):
        super().__init__(msg)

