import unittest

from app.tripulacao.tecnica.oficial import Oficial
from app.tripulacao.tripulacao import Tripulacao


class TestOficial(unittest.TestCase):
    def test_oficial_deve_retornar_um_nome_e_ser_tripulacao(self):

        oficial = Oficial()
        self.assertEqual(oficial.__str__(), 'oficial')
        self.assertIsInstance(oficial, Tripulacao)