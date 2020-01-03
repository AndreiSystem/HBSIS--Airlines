import unittest


from app.tripulacao.cabine.chefe_de_servico import ChefeDeServico
from app.tripulacao.tripulacao import Tripulacao


class TestChefeDeServico(unittest.TestCase):
    def test_chefe_de_servico_deve_retornar_um_nome_e_ser_tripulacao(self):

        chefe_de_servico = ChefeDeServico()

        self.assertEqual(chefe_de_servico.__str__(), 'chefe de serviço')
        self.assertIsInstance(chefe_de_servico, Tripulacao)
