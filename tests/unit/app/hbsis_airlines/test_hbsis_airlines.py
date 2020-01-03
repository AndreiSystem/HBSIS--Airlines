import unittest


from unittest.mock import MagicMock

from app.hbsis_airlines.hbsis_airlines import HbsisAirlines

from app.smart_fortwo.smart_fortwo import SmartFortwo


class TestHbsisAirlines(unittest.TestCase):

    def setUp(self):
        self.hbsis_airlines = HbsisAirlines()
        self.smart_fortwo = SmartFortwo()

    def test_combinacao_valida_piloto_e_oficial(self):
        mock = MagicMock()
        mock2 = MagicMock()

        mock_piloto = mock.__str__.return_value = 'piloto'
        mock_oficial = mock2.__str__.return_value = 'oficial'

        self.hbsis_airlines.get_smart_fortwo().adicionar(mock_piloto)
        self.hbsis_airlines.get_smart_fortwo().adicionar(mock_oficial)

        tripulantes = self.hbsis_airlines.get_tripulacao_no_smart_fortwo()

        self.assertEqual(str(tripulantes[0]), 'piloto')
        self.assertEqual(str(tripulantes[1]), 'oficial')

    def test_combinacao_valida_chefe_e_comissaria(self):
        mock = MagicMock()
        mock2 = MagicMock()

        mock_chefe = mock.__str__.return_value = 'chefe de serviço'
        mock_comissaria = mock2.__str__.return_value = 'comissária'

        self.hbsis_airlines.get_smart_fortwo().adicionar(mock_chefe)
        self.hbsis_airlines.get_smart_fortwo().adicionar(mock_comissaria)

        self.hbsis_airlines.verificacao_combinacao_permitida()

        tripulacao = self.hbsis_airlines.get_tripulacao_no_smart_fortwo()

        self.assertEqual(str(tripulacao[0]), 'chefe de serviço')
        self.assertEqual(str(tripulacao[1]), 'comissária')

    def test_resposta_usuario(self):
        pass