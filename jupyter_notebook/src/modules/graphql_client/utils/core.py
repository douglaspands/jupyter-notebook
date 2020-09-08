"""
Utilitarios para tratamento de query no GraphQL
"""
import json
import re
from datetime import date, datetime, time
from typing import Any, Dict, List, Optional, Union

REGEX_INTERPOLATION_LIST = re.compile(r"{{\s*\w+\s*}}")
REGEX_INTERPOLATION_KEY = re.compile(r"{{\s*(\w+)\s*}}")


def dict_to_graphql(dict_: Dict[str, Any]) -> Dict[str, Any]:
    """Transformar variavel do tipo dict em graphql_dict.

    :param dict_:
    :type dict_: Dict[str, Any]
    :raises TypeError: Parametro de entrada com erro
    :return:
    :rtype: Dict[str, Any]
    """
    if not isinstance(dict_, dict):
        raise TypeError('É obrigatorio passar um parametro no formato "dict"')

    graphql_dict = dict()

    def primitive_format(arg: Union[str, bool, int, float]) -> str:
        return json.dumps(arg, default=str, ensure_ascii=True)

    def date_format(arg: Union[date, datetime, time]) -> str:
        if isinstance(arg, date):
            return arg.strftime('%Y-%m-%d')
        elif isinstance(arg, datetime):
            return arg.strftime('%Y-%m-%dT%H:%M:%S.%f')
        else:
            return arg.strftime('%H:%M:%S')

    def other_format(arg: Any) -> str:
        return json.dumps(arg, default=str, ensure_ascii=True)

    def dict_format(args: Dict[str, Any]) -> str:
        dict_text = "{"
        for num, key in enumerate(args):
            if num > 0:
                dict_text += ", "
            value = args.get(key)
            if isinstance(value, dict):
                dict_text += "{0}: {1}".format(key, dict_format(value))
            elif isinstance(value, list):
                dict_text += "{0}: {1}".format(key, list_format(value))
            elif isinstance(value, (date, datetime, time)):
                dict_text += "{0}: {1}".format(key, date_format(value))
            elif isinstance(value, (str, bool, int, float)):
                dict_text += "{0}: {1}".format(key, primitive_format(value))
            else:
                dict_text += "{0}: {1}".format(key, other_format(value))
        dict_text += "}"
        return dict_text

    def list_format(args: List[Any]) -> str:
        list_text = "["
        for num, value in enumerate(args):
            if num > 0:
                list_text += ", "
            if isinstance(value, dict):
                list_text += "{0}".format(dict_format(value))
            elif isinstance(value, list):
                list_text += "{0}".format(list_format(value))
            elif isinstance(value, (date, datetime, time)):
                list_text += "{0}".format(date_format(value))
            elif isinstance(value, (str, bool, int, float)):
                list_text += "{0}".format(primitive_format(value))
            else:
                list_text += "{0}".format(other_format(value))
        list_text += "]"
        return list_text

    for key, value in dict_.items():
        if isinstance(value, dict):
            graphql_dict.update({key: dict_format(value)})
        elif isinstance(value, list):
            graphql_dict.update({key: list_format(value)})
        elif isinstance(value, (date, datetime, time)):
            graphql_dict.update({key: date_format(value)})
        elif isinstance(value, (str, bool, int, float)):
            graphql_dict.update({key: primitive_format(value)})

    return graphql_dict


def dict_to_hstore(dict_: Dict[str, Any]) -> Dict[str, str]:
    """Transformar variavel do tipo dict em hstore.

    :param dict_:
    :type dict_: Dict[str, Any]
    :raises TypeError: Parametro de entrada com erro
    :return:
    :rtype: Dict[str, str]
    """
    if not isinstance(dict_, dict):
        raise TypeError('É obrigatorio passar um parametro no formato "dict"')

    hstore_dict = dict()

    def date_format(arg: Union[date, datetime, time]) -> str:
        if isinstance(arg, date):
            return arg.strftime('%Y-%m-%d')
        elif isinstance(arg, datetime):
            return arg.strftime('%Y-%m-%dT%H:%M:%S.%f')
        else:
            return arg.strftime('%H:%M:%S')

    for key, value in dict_.items():
        if isinstance(value, str):
            hstore_dict.update({key: value})
        elif isinstance(value, (date, datetime, time)):
            hstore_dict.update({key: date_format(value)})
        else:
            hstore_dict.update({key: json.dumps(value, default=str, ensure_ascii=True)})

    return hstore_dict


def graphilify(graphql_response: Optional[Dict[str, Any]] = None) -> dict:
    """Transformar o "dict" em um "dict graphile"

    :param graphql_response: dict desnormalizado
    :type graphql_response: dict

    :return: dict normalizado para graphile
    :rtype: dict
    """
    # Validar parametros de entrada passado
    if not isinstance(graphql_response, dict):
        raise Exception('É obrigatorio passar um parametro no formato "dict"')

    # Preparando resultado
    dict_new = dict()

    # Tratar dicionario
    def tratar_dicionario(args: Dict[str, Any]) -> str:
        """Tratar dicionario

        :param args:
        :type args: Dict[str, Any]
        :return:
        :rtype: str
        """
        dict_text = "{"
        for num, key in enumerate(args):
            if num > 0:
                dict_text += ", "
            if isinstance(args.get(key), (dict, list)):
                dict_text += f"{key}: " + json.dumps(
                    json.dumps(args.get(key), default=str, ensure_ascii=True),
                    default=str,
                    ensure_ascii=True,
                )
            else:
                dict_text += f"{key}: " + json.dumps(
                    args.get(key), default=str, ensure_ascii=True
                )
        dict_text += "}"
        return dict_text

    # Tratar lista
    def tratar_lista(args: List[Any]) -> str:
        """Tratar lista

        :param args:
        :type args: List[Any]
        :return:
        :rtype: str
        """
        list_text = "["
        for num, value in enumerate(args):
            if num > 0:
                list_text += ", "
            if isinstance(value, (dict, list)):
                list_text += json.dumps(
                    json.dumps(value, default=str, ensure_ascii=True),
                    default=str,
                    ensure_ascii=True,
                )
            else:
                list_text += json.dumps(value, default=str, ensure_ascii=True)
        list_text += "]"
        return list_text

    # Iterar por todo o dicionario
    for key in graphql_response:
        if isinstance(graphql_response[key], dict):
            dict_new.update({key: tratar_dicionario(graphql_response[key])})
        elif isinstance(graphql_response[key], list):
            dict_new.update({key: tratar_lista(graphql_response[key])})
        else:
            dict_new.update(
                {key: json.dumps(graphql_response[key], default=str, ensure_ascii=True)}
            )

    # Retorno
    return dict_new


def interpolation(text: Optional[str] = None, key_value: Optional[Dict[str, Any]] = None) -> str:
    """Executa a interpolação de textos.

    :param text: Texto com parametros de interpolação disponiveis.
    :type key_value: str

    :param key_value: Dicionario com campos que substituirão o texto passado.
    :type key_value: Dict[str, Any]

    :return: Texto substituido pelos campos passados.
    :rtype: str
    """
    # Validar parametros de entrada passado
    if not isinstance(text, str) or not isinstance(key_value, dict):
        raise Exception("Parametros de entrada estão invalidos!")

    # Resultado
    text_new = text

    # Iteração
    for key in REGEX_INTERPOLATION_LIST.findall(text):
        key_ = REGEX_INTERPOLATION_KEY.sub(r"\1", key)
        text_new = text_new.replace(key, key_value.get(key_, "null"))

    # Retorno
    return text_new


def flatten_graphile(key_value: Dict[str, Any]) -> Dict[str, Any]:
    """
    Reduz hierarquias do dict. (Utilizando regras do Postgraphile)
    *obs.: Coleções: Sera considerado o primeiro dict. O restante será removido.

    :param key_value: Dicionario com multiplos nós.
    :type key_value: Dict[str, Any]

    :return: Dicionario com linear
    :rtype: Dict[str, Any]
    """
    # Validação
    if not key_value or not isinstance(key_value, dict):
        return dict()
    # Novo dict
    key_value_new = dict()
    # Para cada key, tratar os sub-nós
    for key in key_value:
        if isinstance(key_value[key], dict):
            key_value_new.update(flatten_graphile(key_value[key]))
        elif isinstance(key_value[key], list) and len(key_value[key]) > 0 and isinstance(key_value[key][0], dict):
            key_value_new.update(flatten_graphile(key_value[key][0]))
        elif key_value[key] is None:
            continue
        else:
            key_value_new[key] = key_value[key]
    # Resultado
    return key_value_new


def flatten(data: Dict[str, Any], always_text: Optional[bool] = False) -> Dict[str, Any]:
    """
    Achatar objetos
    :param data: Dicionario com multiplos nós.
    :type data: dict
    :param always_text: Valores sempre no formato texto (Default: False)
    :type always_text: bool
    :return: Dicionario com linear
    :rtype: dict
    """
    always_text = always_text if isinstance(always_text, bool) else False
    result = dict()

    def recurse(cur, prop):
        if not isinstance(cur, (list, tuple, dict)):
            result[prop] = (
                json.dumps(cur, default=str)
                if always_text is True and not isinstance(cur, str)
                else cur
            )
        elif isinstance(cur, (list, tuple)):
            if len(cur) < 1:
                result[prop] = list()
            else:
                for i, value in enumerate(cur):
                    recurse(value, f"{prop}.{i}" if prop else f"{i}")
        else:
            is_empty = True
            for key, value in cur.items():
                is_empty = False
                recurse(value, f"{prop}.{key}" if prop else key)
            if is_empty:
                result[prop] = dict()

    recurse(data, "")
    return result


def query_clean(query: str) -> str:
    """
    Higienizar GraphQL Query, removendo excesso de caracteres. (espaços, tabulações, enters, etc...)
    :param query: GraphQL Query.
    :type query: str
    :return: GraphQL Query higienizada.
    :rtype: str
    """
    if not isinstance(query, str):
        return str()

    query_ = query
    query_ = re.sub(r"[\t\n\r]", " ", query_)
    query_ = re.sub(r"\s{2,}", " ", query_)
    query_ = query_.strip()
    return query_
