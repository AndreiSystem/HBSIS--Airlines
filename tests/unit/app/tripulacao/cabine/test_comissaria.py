import unittest

from app.tripulacao.cabine.comissaria import Comissaria
from app.tripulacao.tripulacao import Tripulacao


class TestComissaria(unittest.TestCase):
    def test_comissaria_deve_retornar_um_nome_e_ser_tripulacao(self):


        comissaria = Comissaria()

        self.assertEqual(comissaria.__str__(), 'comissária')
        self.assertIsInstance(comissaria, Tripulacao)