import unittest

from app.tripulacao.cabine.chefe_servico import ChefeServico
from app.tripulacao.tripulante import Tripulante


class TestChefeDeServico(unittest.TestCase):
    def test_chefe_de_servico_deveria_ter_um_nome_e_ser_um_tripulante(self):
        nome = 'chefe'

        chefe_servico = ChefeServico(nome)

        self.assertEqual(chefe_servico.get_nome(), 'chefe')
        self.assertIsInstance(chefe_servico, Tripulante)