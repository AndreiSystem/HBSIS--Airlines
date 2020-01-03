import unittest, pytest
from unittest.mock import Mock, MagicMock

from app.exceptions import CapacidadeMaximaDoSmartFortwoExcedidaException
from app.smart_fortwo.smart_fortwo import SmartFortwo



class TestSmartFortwo(unittest.TestCase):
    def test_smart_fortwo_deve_ter_2_tripulantes(self):

        smart_fortwo = SmartFortwo()

        tripulante1_mock = Mock()
        tripulante2_mock = Mock()

        smart_fortwo.adicionar(tripulante1_mock)
        smart_fortwo.adicionar(tripulante2_mock)

        self.assertEqual(len(smart_fortwo.get_tripulantes()), 2)

    def test_smart_fortwo_deveria_ter_somente_2_tripulantes(self):
        smart_fortwo = SmartFortwo()
        tripulante_1_mock = Mock()
        tripulante_2_mock = Mock()
        tripulante_3_mock = Mock()
        with pytest.raises(CapacidadeMaximaDoSmartFortwoExcedidaException) as ex:
            smart_fortwo.adicionar(tripulante_1_mock)
            smart_fortwo.adicionar(tripulante_2_mock)
            smart_fortwo.adicionar(tripulante_3_mock)

        tripulantes = smart_fortwo.get_tripulantes()
        self.assertEqual(len(tripulantes), 2)
        self.assertEqual(str(ex.value), 'Capacidade maxima do smart fortwo excedida')

    def test_verifica_se_piloto_ou_chefe_de_servico_esta_dirigindo(self):

        smart_fortwo = SmartFortwo()
        mock = MagicMock()
        mock2 = MagicMock()

        mock_piloto = mock.__str__.return_value = 'piloto'
        mock_chefe_servico = mock2.__str__.return_value = 'chefe de serviço'

        smart_fortwo.adicionar(mock_piloto)
        smart_fortwo.adicionar(mock_chefe_servico)

        tripulantes = smart_fortwo.get_tripulantes()

        self.assertEqual(tripulantes[0], 'piloto')
        self.assertEqual(tripulantes[1], 'chefe de serviço')

    def test_piloto_difrente_de_comissaria(self):
        smart_fortwo = SmartFortwo()
        mock = MagicMock()
        mock2 = MagicMock()

        mock_piloto = mock.__str__.return_value = 'piloto'
        mock_comissaria = mock2.__str__.return_value = 'comissaria'

        smart_fortwo.adicionar(mock_piloto)
        smart_fortwo.adicionar(mock_comissaria)

        tripulantes = smart_fortwo.get_tripulantes()

        self.assertNotEqual(tripulantes[0], tripulantes[1])