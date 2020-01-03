import unittest

from app.tripulacao.policial_prisioneiro.prisioneiro import Prisioneiro
from app.tripulacao.tripulacao import Tripulacao


class TestPrisioneiro(unittest.TestCase):
    def test_prisioneiro_deve_retornar_um_nome_e_ser_um_tripulante(self):
        prisioneiro = Prisioneiro()


        self.assertEqual(prisioneiro.__str__(), 'prisioneiro')
        self.assertIsInstance(prisioneiro, Tripulacao)