import os, sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sequence import get_fibonacci

class TestUtilsSequence(unittest.TestCase):

    def test_valor_0_sucesso(self):
        """
        get_sequence_fibonacci()
        1 - Passa ordem 0 e retorna 0 com sucesso.
        """
        result = get_fibonacci(0)
        self.assertEqual(result, 0)

    def test_valor_1_sucesso(self):
        """
        get_fibonacci()
        2 - Passa ordem 1 e retorna 1 com sucesso.
        """
        result = get_fibonacci(1)
        self.assertEqual(result, 1)

    def test_valor_2_sucesso(self):
        """
        get_fibonacci()
        3 - Passa ordem 2 e retorna 1 com sucesso.
        """
        result = get_fibonacci(2)
        self.assertEqual(result, 1)

    def test_valor_3_sucesso(self):
        """
        get_fibonacci()
        4 - Passa ordem 3 e retorna 2 com sucesso.
        """
        result = get_fibonacci(3)
        self.assertEqual(result, 2)

    def test_valor_4_sucesso(self):
        """
        get_fibonacci()
        5 - Passa ordem 4 e retorna 3 com sucesso.
        """
        result = get_fibonacci(4)
        self.assertEqual(result, 3)

    def test_valor_invalido_erro(self):
        """
        get_fibonacci()
        6 - Passa texto no lugar da ordem e retorna 0.
        """
        result = get_fibonacci("texto")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
