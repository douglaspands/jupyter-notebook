import os, sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from modules import utils

class TestDicts(unittest.TestCase):

    def test_dict_to_keyhash(self):
        """1-teste de sucesso"""
        try:
            fields = {
                'campo_text': "João é irmão caçula do João do Caminhão",
                'campo_list': [
                    {
                        'campo_text': "João é irmão caçula do João do Caminhão",
                    }
                ],
                'campo_dict': {
                    'campo_text_2': "João é irmão caçula do João do Caminhão",
                }
            }
            result = utils.dicts.dict_to_keyhash(fields, True)
            self.assertEqual(True, True)
        except Exception as error:
            self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()