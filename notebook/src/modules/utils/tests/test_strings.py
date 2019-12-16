import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strings import replace_tags, replace_latin_characters, search_text, interpolation, b64encode


class TestUtilsString(unittest.TestCase):

    def test_01_replace_tag_success(self):
        """1-teste de sucesso"""
        text = "Meu nome é {{nome}} {{ segundo_nome}} {{terceiro_nome }} {{ quarto_nome }} {{       sobrenome  }}"
        fields = {
            'nome': "Joao",
            'segundo_nome': "Pereira",
            'terceiro_nome': "De Albuquerque",
            'quarto_nome': "Da Silva",
            'sobrenome': "e Silva"
        }
        result = replace_tags(text, fields)
        self.assertEqual(result, "Meu nome é Joao Pereira De Albuquerque Da Silva e Silva")

    def test_02_replace_tag_error_1(self):
        """2-Não foram passado todos os campos para substituição"""
        text = "Meu nome é {{nome}} {{ segundo_nome}} {{terceiro_nome }} {{ quarto_nome }} {{       sobrenome  }}"
        fields = {
            'nome': "Joao",
            'terceiro_nome': "De Albuquerque",
            'quarto_nome': "Da Silva",
            'sobrenome': "e Silva"
        }
        result = replace_tags(text, fields)
        self.assertEqual(result, "Meu nome é Joao  De Albuquerque Da Silva e Silva")

    def test_03_replace_tag_error_2(self):
        """3-Texto não foi passado"""
        text = None
        fields = {
            'nome': "Joao",
            'segundo_nome': "Pereira",
            'terceiro_nome': "De Albuquerque",
            'quarto_nome': "Da Silva",
            'sobrenome': "e Silva"
        }
        result = replace_tags(text, fields)
        self.assertEqual(result, "")

    def test_04_replace_tag_error_3(self):
        """4-teste de sucesso"""
        text = "Meu nome é {{nome}} {{ segundo_nome}} {{terceiro_nome }} {{ quarto_nome }} {{       sobrenome  }}"
        fields = None
        result = replace_tags(text, fields)
        self.assertEqual(result, "")

    def test_05_replace_latin_characters_ok(self):
        """4-Substituição de caracteres com acentos, cedilha, etc..."""
        text = 'Você é o "irmão" \'caçula\' do João do Caminhão?'
        result = replace_latin_characters(text)
        expect = 'Voce e o "irmao" \'cacula\' do Joao do Caminhao?'
        self.assertEqual(result, expect)

    def test_06_pesquisar_texto_ok(self):
        """5-Pesquisar textos"""
        words = 'Voce e o "irmao" \'cacula\' do Joao do Caminhao?'
        text = 'Você é o "irmão" \'caçula\' do João do Caminhão?'
        result = search_text(words, text, False, True)
        self.assertEqual(result, True)

    def test_07_pesquisar_texto_excesso_espacos_ok(self):
        """6-Pesquisar textos desconsiderando excesso de espaços"""
        words = 'Voce    e    o    "irmao"     \'cacula\'     do    Joao    do    Caminhao?'
        text = 'Você é o "irmão" \'caçula\' do João do Caminhão?'
        result = search_text(words, text, False, True, True)
        self.assertEqual(result, True)

    def test_08_pesquisar_texto_nok(self):
        """7-Pesquisar textos e não encontrar"""
        words = 'Voce e "irmao" \'cacula\' do Joao do Caminhao?'
        text = 'Você é o "irmão" \'caçula\' do João do Caminhão?'
        result = search_text(words, text, False, True)
        self.assertEqual(result, False)

    def test_09_pesquisar_texto_escape_ok(self):
        """7-Pesquisar textos considerando caracteres escape (com excesso de espaços sem case sensitive)"""
        words = 'não conta(m) processo(s)'
        text = '  FULANO DE TAL     NAO  CONTA(m)     PROCESSO(s)     EM ABERTO'
        result = search_text(words, text, False, True, True)
        self.assertEqual(result, True)

    def test_09_pesquisar_texto_escape_ok2(self):
        """8-Pesquisar textos considerando caracteres escape (com excesso de espaços sem case sensitive)"""
        words = 'não conta(m)   processo(s)'
        text = '  FULANO DE TAL     NAO  CONTA(m)     PROCESSO(s)     EM ABERTO'
        result = search_text(words, text, False, True, True)
        self.assertEqual(result, True)

    def test_10_interpolation(self):
        """9-teste de sucesso"""
        text = "Meu nome é {{nome}} {{ segundo_nome}} {{terceiro_nome }} {{ quarto_nome }} {{       sobrenome  }}"
        fields = {
            'nome': "Joao",
            'segundo_nome': "Pereira",
            'terceiro_nome': "De Albuquerque",
            'quarto_nome': "Da Silva",
            'sobrenome': "e Silva"
        }
        result = interpolation(text, fields)
        self.assertEqual(result, "Meu nome é Joao Pereira De Albuquerque Da Silva e Silva")

    def test_11_b64encode(self):
        """11-Testar geração de encodin"""
        text = 'douglaspanhota:TWFyY2VsbzE6MDU4ZWNiYWYtNDFlZC00ZDY4LThlOGEtNmM3NmU1NTNlY2Vj'
        result = b64encode(text)
        self.assertEqual(result, 'TWFyY2VsbzE6MDU4ZWNiYWYtNDFlZC00ZDY4LThlOGEtNmM3NmU1NTNlY2Vj')


if __name__ == '__main__':
    unittest.main()