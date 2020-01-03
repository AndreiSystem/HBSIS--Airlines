class Aviao:
    def __init__(self):
        self._aviao = []

    def get_tripulantes_no_aviao(self):
        return self._aviao

    def quantidade_de_passageiros_no_aviao(self):
        return len(self._aviao)

    def adicionar_no_aviao(self, tripulantes: list):
        tripulante_no_aviao = tripulantes.pop(1)

        self._aviao.append(tripulante_no_aviao)

    def mostrar_passageiros_do_aviao(self):
        c = 1
        for i in self.get_tripulantes_no_aviao():
            print(f'\033[1;33m[{c}]\033[m {str(i).capitalize()}')
            c+=1

    def retirar_do_aviao(self, n, smart_fortwo=None):

        smart_fortwo.adicionar(self._aviao.pop(n-1))






