import unittest
from unittest.mock import Mock, MagicMock, patch

from app.aviao.aviao import Aviao
from app.smart_fortwo.smart_fortwo import SmartFortwo



class TestAviao(unittest.TestCase):


    def test_aviao_deve_estar_vazio(self):
        aviao = Aviao()

        self.assertEqual(0, aviao.quantidade_de_passageiros_no_aviao())


    def test_verifica_se_passageiro_esta_no_aviao(self):

        smart_fortwo = SmartFortwo()
        aviao = Aviao()

        mock = MagicMock()
        mock2 = MagicMock()

        mock_piloto = mock.__str__.return_value = 'piloto'
        mock_oficial = mock2.__str__.return_value = 'oficial'

        smart_fortwo.adicionar(mock_piloto)
        smart_fortwo.adicionar(mock_oficial)

        tripulantes = smart_fortwo.get_tripulantes()

        aviao.adicionar_no_aviao(tripulantes)

        self.assertIn('oficial', aviao.get_tripulantes_no_aviao())

    def test_retirar_do_aviao(self):
        aviao = Aviao()

        aviao.adicionar_no_aviao(Mock())
        aviao.adicionar_no_aviao(Mock())

        aviao.retirar_do_aviao(1, SmartFortwo())


        self.assertEqual(1, aviao.quantidade_de_passageiros_no_aviao())

    def test_get_quantidade_de_passageiros_no_aviao_should_be_return_zero(self):

        aviao = Aviao()

        self.assertEqual(0, aviao.quantidade_de_passageiros_no_aviao())

    def test_get_quantidade_de_passageiros_no_aviao_should_be_return_four(self):

        aviao = Aviao()
        aviao.adicionar_no_aviao(Mock())
        aviao.adicionar_no_aviao(Mock())
        aviao.adicionar_no_aviao(Mock())
        aviao.adicionar_no_aviao(Mock())

        self.assertEqual(4, aviao.quantidade_de_passageiros_no_aviao())

    def test_mostrar_passageiros_que_estao_dentro_do_aviao(self):

        aviao = Aviao()

        aviao.adicionar_no_aviao(Mock())
        aviao.adicionar_no_aviao(Mock())

        aviao.mostrar_passageiros_do_aviao()
