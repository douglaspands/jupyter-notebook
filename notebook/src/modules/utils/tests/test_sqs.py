import os, sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.sqs import time_delay

class TestUtilsSQS(unittest.TestCase):

    def test_seq_0_ok(self):
        """
        time_delay()
        1 - Passa ordem 0 e retorna 60 (seg) com sucesso.
        """
        result = time_delay(0)
        self.assertEqual(result, 60)

    def test_seq_1_ok(self):
        """
        time_delay()
        2 - Passa ordem 1 e retorna 60 (seg) com sucesso.
        """
        result = time_delay(1)
        self.assertEqual(result, 60)

    def test_seq_menor_0_ok(self):
        """
        time_delay()
        3 - Passa ordem -1 e retorna 60 (seg) com sucesso.
        """
        result = time_delay(-1)
        self.assertEqual(result, 60)

    def test_seq_3_ok(self):
        """
        time_delay()
        4 - Passa ordem 3 e retorna 120 (seg) com sucesso.
        """
        result = time_delay(3)
        self.assertEqual(result, 120)

    def test_seq_7_ok(self):
        """
        time_delay()
        5 - Passa ordem 7 e retorna 780 (seg) com sucesso.
        """
        result = time_delay(7)
        self.assertEqual(result, 780)

    def test_seq_8_ok(self):
        """
        time_delay()
        6 - Passa ordem 8 e retorna 900 (seg) (max) com sucesso.
        """
        result = time_delay(8)
        self.assertEqual(result, 900)

    def test_seq_12_ok(self):
        """
        time_delay()
        7 - Passa ordem 12 e retorna 900 (seg) (max) com sucesso.
        """
        result = time_delay(12)
        self.assertEqual(result, 900)

    def test_seq_invalid1_ok(self):
        """
        time_delay()
        8 - Passa ordem invalido e retorna 60 (seg) com sucesso.
        """
        result = time_delay('A')
        self.assertEqual(result, 60)

    def test_seq_invalid2_ok(self):
        """
        time_delay()
        9 - Passa ordem invalido e retorna 60 (seg) com sucesso.
        """
        result = time_delay(True)
        self.assertEqual(result, 60)

    def test_seq_invalid3_ok(self):
        """
        time_delay()
        10 - Passa ordem invalido e retorna 60 (seg) com sucesso.
        """
        result = time_delay(False)
        self.assertEqual(result, 60)

if __name__ == '__main__':
    unittest.main()
