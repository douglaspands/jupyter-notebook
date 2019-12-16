"""
Modulo de tratamento de XML.
"""
__all__ = [
    'dict_to_xml'
]

import re
import logging
import xml.sax.saxutils as xml

logger = logging.getLogger(__name__)


def dict_to_xml(json: dict) -> str:
    """
    Transformar JSON/Dict em XML.
    :param json: objeto json/dict
    :return: xml
    """
    # Validar se foram passados todos os parametros solicitados
    if not isinstance(json, dict):
        logger.error(f'{__name__}: Parametro de entrada "json" do tipo "dict" invalido!')
        return ''

    # Tratar root do xml
    _json = dict()
    _json['root'] = json

    # Corpo do XML
    xml_body = ''

    # Criando buffer de texto
    for key, value in dict(_json['root']).items():
        xml_body += _param_to_elem(key, value)

    # Concatenando o header com o body
    xml_final = '<?xml version="1.0" encoding="utf-8"?>\n' + xml_body

    # Logging do resultado final
    logger.debug(f'{__name__}: resultado:\n{xml_final}')

    # Retornado resultado
    return xml_final


def _param_to_elem(key: str, value):
    """
    Transformando parametro dict em elemento xml.
    :param key: nome do campo
    :param value: valor do campo
    """
    # Transformar chave em texto
    _key_ini = str(key)
    _key_end = re.compile(r'\s|\>').split(_key_ini)[0]

    # Valor do tipo booleano
    if isinstance(value, bool):
        _value = _treat_value('true' if value else 'false')
        return f'<{_key_ini}>{_value}</{_key_end}>'

    # Valor do tipo inteiro ou float
    elif isinstance(value, int) or isinstance(value, float):
        _value = _treat_value(str(value))
        return f'<{_key_ini}>{_value}</{_key_end}>'

    # Valor do tipo texto
    elif isinstance(value, str):
        if not value:
            return f'<{_key_ini}></{_key_end}>'
        else:
            _value = _treat_value(value)
            return f'<{_key_ini}>{_value}</{_key_end}>'

    # Valor do tipo lista
    elif isinstance(value, list):
        _value = list(map(lambda v: _param_to_elem(_key_ini, v), value))
        return ''.join(_value)

    # Valor do tipo dict
    elif isinstance(value, dict):

        # extraparam
        fl_extra_param = False
        for k in value.keys():
            if bool(re.search(r'^@|#', k)):
                fl_extra_param = True
                break

        # Tratar tag com atributos
        if fl_extra_param:

            _key_attr = f'{_key_ini}'
            _text = '' if '#text' not in value else value['#text']

            # Tratamento do CDATA
            if '#cdata' in value and value['#cdata'] is True and _text:
                _text = _include_cdata(str(_text))

            # Tratar atributos do elemento
            for k, v in value.items():

                # Verificar sintaxe dos atributos
                if bool(re.search(r'^@', str(k))):

                    _attr = str(k.replace('@', ''))
                    _key_attr += f' {_attr}="{str(v)}"'

            # Tratar valor do atributo novo
            _value = _param_to_elem(_key_attr, _text)
            return _value

        # Tratar tag sem atributos
        else:
            _value = f'<{_key_ini}>'
            for k, v in value.items():
                _value += _param_to_elem(k, v)
            _value += f'</{_key_end}>'
            return _value

    # Quando não for um tipo permitido
    else:
        return f'<{_key_ini}></{_key_end}>'


def _include_cdata(value: str) -> str:
    """
    Incluir cdata.
    :param value: Valor do contexto.
    :return: valor com cdata.
    """
    _value = f'<![CDATA[{str(value)}]]>'
    return _value


def _treat_value(value: str) -> str:
    """
    Tratar valor do contexto do elemento.
    :param value: Valor do contexto.
    :return: valor tratado.
    """
    _value = _text_normalize(value)

    # Ignorar validação de escape no XML quando CDATA estiver disponivel
    if not bool(re.search(r'^\<\!\[CDATA\[', _value)) and \
       not bool(re.search(r'\]\]\>$', _value)):
        _value = xml.escape(_value)

    return _value


def _text_normalize(text: str) -> str:
    """
    Normalização do texto em 'utf-8'.
    :param text:
    :return: Texto normalizado.
    """
    text_enc = text.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
    char_list = []
    for c in text_enc:
        if c in ['\n', '\t'] or c.isprintable():
            char_list.append(c)
    text_new = ''.join(char_list)
    return text_new


def create_element(value, cdata: bool = False, attr: dict = {}) -> dict:
    """
    Criar elemento no XML.

    :type value: any
    :param value: Valor atribuido no elemento.

    :type cdata: bool
    :param cdata:

    :type attr: dict
    :param attr:

    :rtype: dict
    :return: Objeto que representa o elemento

    """

    if not isinstance(cdata, bool) or not isinstance(attr, dict):
        raise Exception(f'{__name__}: Parametros de criação do elemento invalidos!')

    element = dict()

    element['#text'] = value
    element['#cdata'] = True if cdata is True else False

    for _k, _v in attr.items():
        element[f'@{_k}'] = str(_v)

    return element

