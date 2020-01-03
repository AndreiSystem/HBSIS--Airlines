import time

from app.aviao.aviao import Aviao
from app.smart_fortwo.smart_fortwo import SmartFortwo
from app.terminal.terminal import Terminal


class HbsisAirlines:
    def __init__(self):
        self._terminal = Terminal()
        self._smart_fortwo = SmartFortwo()
        self._aviao = Aviao()

        self._tripulacao_aviao = self._aviao.get_tripulantes_no_aviao()

        self._tripulacao = self._terminal.get_tripulantes()

    def start(self):

        while True:
            self.painel()

            motorista = self.resposta_usuario(self._tripulacao)
            self._smart_fortwo.adicionar(motorista)

            self.painel()

            passageiro = self.resposta_usuario(self._tripulacao)
            self._smart_fortwo.adicionar(passageiro)

            self.verificacao_combinacao_permitida()

            print()
            print('----- Tripulantes no SmartFortwo -----')
            self.get_tripulantes_embarcados_no_smart_fortwo()


            input('----- Pressione \033[1;32m[ENTER]\033[m para ir até o estino! -----')
            _loading()

            self._aviao.adicionar_no_aviao(self._smart_fortwo.get_tripulantes())

            print()
            print('----- Tripulantes no avião -----')
            self.get_tripulacao_no_aviao()


            self.resposta_usuario_aviao()

            if self._aviao.quantidade_de_passageiros_no_aviao() == 8:
                print('\033[1;32mFinalzado com Sucesso!\033[m')
                print(f'\033[1;32mTripulantes Embarcados: \033[m{self._aviao.quantidade_de_passageiros_no_aviao()}')
                break

            input('----- Pressione \033[1;32m[ENTER]\033[m para voltar ao terminal! -----')
            _loading()

            self.retorna_motorista()

    def get_smart_fortwo(self):
        return self._smart_fortwo

    def painel(self):
        print('Tripulação no Terminal: ')
        print(f"{'-'*25}")
        c = 1
        for i in self._terminal.get_tripulantes():
            print(f'\033[1;33m[{c}]\033[m {str(i).capitalize()}')
            c+=1

    def verificacao_combinacao_permitida(self):
        tripulacao = self._smart_fortwo.get_tripulantes()

        while True:
            _carregando()

            if str(tripulacao[0]) == 'policial' and str(tripulacao[1]) != 'comissária' and str(tripulacao[1]) != 'oficial':
                break
            elif str(tripulacao[0]) == 'piloto' and str(tripulacao[1]) != 'comissária' and str(
                    tripulacao[1]) != 'prisioneiro':
                break
            elif str(tripulacao[0]) == 'chefe de serviço' and str(tripulacao[1]) != 'oficial' and str(
                    tripulacao[1]) != 'prisioneiro':
                break
            else:
                print('Erro de combinação!')
                self._tripulacao.append(self.get_tripulacao_no_smart_fortwo().pop(1))
                self.painel()
                passageiro = self.resposta_usuario(self._tripulacao)
                self._smart_fortwo.adicionar(passageiro)

    def get_tripulacao_no_smart_fortwo(self):
        return self._smart_fortwo.get_tripulantes()

    def get_tripulacao_no_aviao(self):
        for i in self._aviao.get_tripulantes_no_aviao():
            print(str(i).capitalize())

    def retorna_motorista(self):
        motorista = self.get_tripulacao_no_smart_fortwo().pop(0)

        self._terminal.get_tripulantes().append(motorista)

    def get_tripulantes_embarcados_no_smart_fortwo(self):
        tripulacao = self.get_tripulacao_no_smart_fortwo()

        print(f'Motorista: {str(tripulacao[0]).capitalize()}')
        print(f'Passageiro: {str(tripulacao[1]).capitalize()}')


    def resposta_usuario(self, tripulacao: list):
        while True:
            try:
                resp = int(input('Digite o Número da tripulação que vai embarcar: '))
                return tripulacao.pop(resp-1)

            except ValueError:
                print('Apenas números Inteiros!')
            except:
                print('Tripulante Inexistente!')

    def resposta_usuario_aviao(self):
        controler = True
        while controler:
            try:
                print('----------------------------------')
                print('\033[1;33m[1]\033[m - Voltar com o motorista atual')
                print('\033[1;33m[2]\033[m - Descer motorista')
                print('----------------------------------')

                resp = int(input('Escolha uma das opções: '))
                if resp == 1:
                    break

                elif resp == 2:
                    motorista = self.get_tripulacao_no_smart_fortwo().pop()

                    self._tripulacao_aviao.append(motorista)

                    self._aviao.mostrar_passageiros_do_aviao()

                    if self._aviao.quantidade_de_passageiros_no_aviao() == 8:
                        controler = False
                        return controler
                    else:

                        passageiro = int(input('Digite a posição de qual Tripulante gostaria de retornar: '))
                        self._aviao.retirar_do_aviao(passageiro, self._smart_fortwo)

                else:
                    raise Exception('Essa opção não existe!')

            except ValueError:
                print('\033[1;31m Apenas números Inteiros! \033[m')
            except Exception as e:
                print(f'\033[1;31m Alerta: {e} \033[m')

    def retirar_do_aviao(self, n):
        self._smart_fortwo.adicionar(self._aviao.get_tripulantes_no_aviao().pop(n-1))


def _carregando():
    for i in range(11):
        print(f'Verificando \033[1;32m{i}%...\033[m')
        time.sleep(0.1)
def _loading():
    for i in range(10, 50, 10):
        print(f'{i}KM')
        time.sleep(0.5)
    print()
    print('Chegada ao destino!')









