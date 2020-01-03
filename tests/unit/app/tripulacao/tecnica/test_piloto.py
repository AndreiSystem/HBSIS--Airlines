import unittest

from app.tripulacao.tecnica.piloto import Piloto
from app.tripulacao.tripulacao import Tripulacao


class TestPiloto(unittest.TestCase):
    def test_piloto_deve_retornar_um_nome_e_ser_tripulacao(self):

        piloto = Piloto()
        self.assertEqual(piloto.__str__(), 'piloto')
        self.assertIsInstance(piloto, Tripulacao)