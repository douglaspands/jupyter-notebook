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
xml = utils.xmls


# Classe de testes
class TestUtilsXmls(unittest.TestCase):
    """Classe de testes do WebDriver"""

    def test_validar_parametros_entrada(self):
        """
        Parametro de entrada invalido.
        """
        _json = True
        result = xml.dict_to_xml(_json)
        expect = ''
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_simples_texto(self):
        """
        Transformar elemento simples de texto em xml
        """
        _json = dict()
        _json['elemento1'] = 'teste'
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento1>teste</elemento1>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_simples_texto_escape(self):
        """
        Transformar elemento simples de texto (com escape) em xml
        """
        _json = dict()
        _json['elemento1'] = '<teste>'
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento1>&lt;teste&gt;</elemento1>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_simples_integer(self):
        """
        Transformar elemento simples de integer em xml
        """
        _json = dict()
        _json['elemento1'] = 2
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento1>2</elemento1>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_simples_float(self):
        """
        Transformar elemento simples de float em xml
        """
        _json = dict()
        _json['elemento1'] = -23.1212
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento1>-23.1212</elemento1>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_simples_boolean_true(self):
        """
        Transformar elemento simples de boolean (True) em xml
        """
        _json = dict()
        _json['elemento1'] = True
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento1>true</elemento1>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_simples_boolean_false(self):
        """
        Transformar elemento simples de boolean (False) em xml
        """
        _json = dict()
        _json['elemento1'] = False
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento1>false</elemento1>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_lista(self):
        """
        Transformar elemento de lista em xml
        """
        _json = dict()
        _json['elemento'] = ['teste1', 'teste2']
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento>teste1</elemento><elemento>teste2</elemento>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_com_atributos(self):
        """
        Inclusão de atributos no elemento XML
        """
        _json = dict()
        _json['elemento'] = {
            '@atributo1': 'attr_teste1',
            '#text': 'valor de teste'
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento atributo1="attr_teste1">valor de teste</elemento>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_com_cdata_paramextra(self):
        """
        Inclusão de CDATA no elemento XML (com parametro especial)
        """
        _json = dict()
        _json['elemento'] = {
            '#cdata': True,
            '#text': '<valor de teste>'
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento><![CDATA[<valor de teste>]]></elemento>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_com_cdata_paramextra_falso(self):
        """
        Inclusão de CDATA no elemento XML (com parametro especial)
        Execução não incluira devido ao parametro não ser do tipo Boolean.
        """
        _json = dict()
        _json['elemento'] = {
            '#cdata': 'True',
            '#text': '<valor de teste>'
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento>&lt;valor de teste&gt;</elemento>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_com_cdata_content(self):
        """
        Inclusão de CDATA no elemento XML (com CDATA no valor)
        """
        _json = dict()
        _json['elemento'] = '<![CDATA[<valor de teste>]]>'
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento><![CDATA[<valor de teste>]]></elemento>'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_valor_invalido(self):
        """
        Passar um valor invalido.
        """
        _json = dict()

        def method_fake():
            pass

        _json['elemento'] = method_fake
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento />'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_valor_vazio(self):
        """
        Passar um valor vazio simples.
        """
        _json = dict()
        _json['elemento'] = ''
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento />'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_valor_htext_vazio(self):
        """
        Passar um valor vazio simples pelo #text.
        """
        _json = dict()
        _json['elemento'] = {
            '#text': ''
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento />'
        self.assertEqual(result, expect)

    def test_criar_xml_elemento_valor_sem_htext(self):
        """
        Não passar um valor vazio simples pelo #text.
        """
        _json = dict()
        _json['elemento'] = {
            '@attr': 'lista'
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<elemento attr="lista" />'
        self.assertEqual(result, expect)

    def test_criar_xml_elementos_complexos(self):
        """
        Criar XML com elementos complexos.
        """
        _json = dict()
        _json['fotos'] = {
            'foto': [
                'foto1',
                'foto2'
            ]
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<fotos><foto>foto1</foto><foto>foto2</foto></fotos>'
        self.assertEqual(result, expect)

    def test_criar_xml_elementos_complexos_htext(self):
        """
        Criar XML com elementos complexos.
        """
        _json = dict()
        _json['fotos'] = {
            '#text': {
                'foto': [
                    'foto1',
                    'foto2'
                ]
            }
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<fotos><foto>foto1</foto><foto>foto2</foto></fotos>'
        self.assertEqual(result, expect)

    def test_criar_xml_elementos_complexos_com_outro_complexo(self):
        """
        Criar XML com elementos complexos.
        """
        _json = dict()
        _json['pessoa'] = {
            'nome': 'Joao',
            'fotos': {
                'foto': [
                    'foto1',
                    'foto2'
                ]
            }
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<pessoa><nome>Joao</nome><fotos>' \
                 '<foto>foto1</foto><foto>foto2</foto></fotos></pessoa>'
        self.assertEqual(result, expect)

    def test_criar_xml_elementos_complexos_com_outro_complexo_htext(self):
        """
        Criar XML com elementos complexos (com #text).
        """
        _json = dict()
        _json['pessoa'] = {
            '#text': {
                'nome': {
                    '#text': 'Joao'
                },
                'fotos': {
                    '#text': {
                        'foto': {
                            '#text': [
                                'foto1',
                                'foto2'
                            ]
                        }
                    }
                }
            }
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<pessoa><nome>Joao</nome><fotos>' \
                 '<foto>foto1</foto><foto>foto2</foto></fotos></pessoa>'
        self.assertEqual(result, expect)

    def test_criar_xml_elementos_complexos_com_outro_complexo_attr_htext(self):
        """
        Criar XML com elementos complexos (com #text).
        """
        _json = dict()
        _json['pessoa'] = {
            '@descricao': "Objeto do tipo pessoa",
            '#text': {
                'nome': {
                    '@descricao': 'Nome da pessoa',
                    '#text': 'Joao'
                },
                'fotos': {
                    '@descricao': 'Lista de fotos',
                    '#text': {
                        'foto': {
                            '#text': [
                                'foto1',
                                'foto2'
                            ]
                        }
                    }
                }
            }
        }
        result = xml.dict_to_xml(_json)
        expect = '<?xml version="1.0" encoding="utf-8"?>\n<pessoa descricao="Objeto do tipo pessoa">' \
                 '<nome descricao="Nome da pessoa">Joao</nome>' \
                 '<fotos descricao="Lista de fotos"><foto>foto1</foto><foto>foto2</foto></fotos></pessoa>'
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
