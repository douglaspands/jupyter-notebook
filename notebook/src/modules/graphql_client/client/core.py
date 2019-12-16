"""
Client de APIs GraphQL.
"""
__all__ = ['request']

# Modulos utilizados
import json
import logging
import requests

# Logger
logger = logging.getLogger(__name__)


def request(url: str, query: str, fields: dict = None, authorization: str = '', timeout: float = 3.001,
            ensure_ascii: bool = True):
    """
    Request GraphQL.
    :param url: Rota de onde vai ser executado a api em GraphQL
    :type url: str
    :param query: Query do GraphQL
    :type query: str
    :param fields: (opcional) Parametros que farão a interpolação do GraphQL
    :type fields: dict
    :param authorization: (opcional) Token para autorização.
    :type authorization: str
    :param timeout: (opcional) Tempo em segundos para disparar o timeout
    :type timeout: float
    :param ensure_ascii: Garantir conversão ASCII. (default: True)
    :type ensure_ascii: bool
    :return: Resultado da request
    :rtype: dict
    """
    # Default de campos
    fields = fields if isinstance(fields, dict) else dict()
    timeout = timeout if isinstance(timeout, float) else 3.001
    ensure_ascii = ensure_ascii if isinstance(ensure_ascii, bool) else True

    # Validação dos parametros de entrada
    if not isinstance(url, str) or not url or not isinstance(query, str) or not query:
        message_error = 'Parametros de entrada não foram passados ou estão invalidos'
        logger.error(message_error)
        raise Exception(f'{message_error}')

    # Parametrizando headers
    headers = dict()
    headers['Content-type'] = 'application/json'
    headers['Accept'] = 'application/json'
    if authorization:
        headers['Authorization'] = f'Bearer {str(authorization)}'

    # Construindo query do client
    payload = {
        'query': __create_query(query, fields)
    }

    # Transformar em string antes de enviar
    data = json.dumps(payload, default=str, ensure_ascii=ensure_ascii)\
        .encode('utf-8', 'ignore').decode('utf-8', 'ignore')

    logger.debug(
        f'Execução com os argumentos:\n> url: {url}\n'
        f'> headers: {repr(headers)}\n'
        f'> timeout: {timeout}\n> payload: {data}')

    # Executando GraphQL
    try:
        response = requests.post(url=url, data=data, headers=headers, timeout=timeout)
        try:
            result = response.json()
        except Exception as error:
            logger.debug(error)
            result = {'errors': [{'message': response.text}]}
    except Exception as error:
        logger.debug(error)
        result = {'errors': [{'message': str(error)}]}
    finally:
        logger.debug(f'Retorno da execução: {json.dumps(result, default=str, indent=4)}')
        return result


def __create_query(query: str, fields: dict = None) -> str:
    """Criar query client incrementando os campos passados pelo dict.
    Tambem efetua uma higienização nos campos.

    :param query: Query Graphql
    :type query: str
    :param fields: Campos desnormalizado
    :type fields: dict
    :return: Query Graphql transformado.
    :rtype: str
    """
    # Imports
    from ..utils import interpolation
    from ..utils import graphilify
    # Transformar query
    if not fields:
        return query
    else:
        return interpolation(query, graphilify(fields))
