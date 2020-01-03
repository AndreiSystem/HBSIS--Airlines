import unittest

from app.terminal.terminal import Terminal



class TestTerminal(unittest.TestCase):
    def test_tripulacao_no_terminal_deve_possuir_8(self):
        terminal = Terminal()

        self.assertEqual(len(terminal.get_tripulantes()), 8)




