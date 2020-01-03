import unittest

from app.tripulacao.policial_prisioneiro.policial import Policial
from app.tripulacao.tripulacao import Tripulacao


class TestPolicial(unittest.TestCase):
    def test_policial_deve_retornar_um_nome_e_ser_tripulacao(self):

        policial = Policial()

        self.assertEqual(policial.__str__(), 'policial')
        self.assertIsInstance(policial, Tripulacao)