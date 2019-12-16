import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from validacao import iptu_sp_verificar_dac


class TestUtilsValidacao(unittest.TestCase):

    def test_iptu_validacao_str_sucesso(self):
        """
        iptu_sp_verificar_dac()
        1 - Teste de sucesso com IPTU no formato string.
        """
        result = iptu_sp_verificar_dac("10141502801")
        self.assertEqual(str(result).isdigit(), True)

    def test_iptu_validacao_int_sucesso(self):
        """
        iptu_sp_verificar_dac()
        2 - Teste de sucesso com IPTU no formato numerico.
        """
        result = iptu_sp_verificar_dac(10141502801)
        self.assertEqual(str(result).isdigit(), True)

    def test_iptu_validacao_dac_errado_erro(self):
        """
        iptu_sp_verificar_dac()
        3 - Teste de erro com dac invalido do IPTU.
        """
        result = iptu_sp_verificar_dac("10141502805")
        self.assertEqual(str(result).isdigit(), False)

    def test_iptu_validacao_maior_11_digitos_erro1(self):
        """
        iptu_sp_verificar_dac()
        4 - Teste de sucesso com numero do IPTU certo 
        porem com muitos zeros esquerda.
        """
        result = iptu_sp_verificar_dac("00000000010141502801")
        self.assertEqual(str(result).isdigit(), False)

    def test_iptu_validacao_maior_11_digitos_erro2(self):
        """
        iptu_sp_verificar_dac()
        5 - Teste de erro com numero do IPTU maior que 11 digitos.
        """
        result = iptu_sp_verificar_dac("12345678910141502801")
        self.assertEqual(str(result).isdigit(), False)

    def test_iptu_validacao_nao_numerico_erro(self):
        """
        iptu_sp_verificar_dac()
        6 - Teste de erro com passando valor não numerico para a função. 
        """
        result = iptu_sp_verificar_dac(True)
        self.assertEqual(str(result).isdigit(), False)

    def test_iptu_validacao_str_invalida_erro(self):
        """
        iptu_sp_verificar_dac()
        7 - Teste de erro com IPTU no formato string errado.
        """
        result = iptu_sp_verificar_dac("101abcd2801")
        self.assertEqual(str(result).isdigit(), False)


if __name__ == '__main__':
    unittest.main()
