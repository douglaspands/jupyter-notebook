import os
import sys
import logging
import unittest
from importlib import import_module

# Configurando o logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
    )

# Mudando o sys.path para testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Import modulo
utils = import_module('modules.utils')
asyncios = utils.asyncios


# Classe de testes
class TestUtilsAsyncios(unittest.TestCase):
    """Classe de testes do WebDriver"""

    def test_validar_parametros_entrada(self):
        """
        Parametro de entrada invalido.
        """

        async def somar(x, y):
            return x + y

        result = asyncios.run(somar(2, 3))
        expect = 5

        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
