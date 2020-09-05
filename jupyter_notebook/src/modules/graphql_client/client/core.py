"""
Client de APIs GraphQL.
"""
import re
import json
import logging
from time import time, sleep
from typing import Dict, Any, Optional

from pydash import _
import requests
import urllib3

from .types import IGraphQLResponse

from ..utils import interpolation
from ..utils import dict_to_graphql


# Logger
logger = logging.getLogger("graphql_client")

# Remoção da mensagem de warning: InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Expressão regular para capturar erro de timeout
regex_timeout = re.compile(r"time\s*out", re.IGNORECASE)


def request(*args, **kwargs) -> IGraphQLResponse:
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
    :param timeout: (opcional) Tempo em segundos para disparar o timeout, (default: 30seg)
    :type timeout: float
    :param ensure_ascii: Garantir conversão ASCII. (default: True)
    :type ensure_ascii: bool
    :param attempts: (opcional) tentativas de execuções em caso de timeout, (default: 1)
    :type attempts: int
    :return: Resultado da request
    :rtype: Union[List[Dict[str, Any]], Dict[str, Any]]
    """
    attempts = kwargs.get('attempts') or 1
    try:
        del kwargs['attempts']
    except KeyError:
        pass
    result: IGraphQLResponse = dict()
    for attempt in range(attempts):
        next_attempt = (attempt + 1)
        logger.debug('Tentativa %s de %s', next_attempt, attempts)
        result = __request(*args, **kwargs)
        if False is bool(regex_timeout.search(str(_.get(result, 'errors[0].message')))) or \
           next_attempt == attempts:
            break
        sleep(10)
    return result


def __request(url: str, query: str, **kwargs: Any) -> IGraphQLResponse:
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
    :param timeout: (opcional) Tempo em segundos para disparar o timeout, (default: 30seg)
    :type timeout: float
    :param ensure_ascii: Garantir conversão ASCII. (default: True)
    :type ensure_ascii: bool
    :return: Resultado da request
    :rtype: Union[List[Dict[str, Any]], Dict[str, Any]]
    """
    # Default de campos
    authorization: str = kwargs.get('authorization') or str()
    fields: Dict[str, Any] = kwargs['fields'] if isinstance(kwargs.get('fields'), dict) else dict()
    timeout: float = kwargs['timeout'] if isinstance(kwargs.get('timeout'), float) else 30.001
    ensure_ascii: bool = kwargs['ensure_ascii'] if isinstance(kwargs.get('ensure_ascii'), bool) else True

    # Validação dos parametros de entrada
    if not isinstance(url, str) or not url or not isinstance(query, str) or not query:
        message_error = "Parametros de entrada não foram passados ou estão invalidos"
        logger.error(message_error)
        raise Exception(f"{message_error}")

    # Parametrizando headers
    headers = dict()
    headers["Content-type"] = "application/json"
    headers["Accept"] = "application/json"
    if authorization:
        headers["Authorization"] = f"Bearer {str(authorization)}"

    # Construindo query do client
    payload = {"query": __query_builder(query, fields)}

    # Transformar em string antes de enviar
    data = (
        json.dumps(payload, default=str, ensure_ascii=ensure_ascii)
        .encode("utf-8", "ignore")
        .decode("utf-8", "ignore")
    )

    logger.debug('Execução com os argumentos:\n> url: %s\n> headers: %s\n> timeout: %s\n> payload: %s',
                 url, repr(headers), timeout, data)

    # Executando GraphQL
    time_end = None
    time_start = time()

    result: IGraphQLResponse = dict()
    try:
        response = requests.post(
            url=url, data=data, headers=headers, timeout=timeout, verify=False
        )
        time_end = time()
        try:
            result = response.json()
        except Exception as error:
            logger.debug(error)
            result = {"errors": [{"message": response.text}]}

    except Exception as error:
        logger.debug(error)
        result = {"errors": [{"message": str(error)}]}

    finally:
        time_end = time_end if time_end else time()
        logger.debug('Retorno da execução: %s', json.dumps(result, default=str, indent=4))
        logger.debug('Tempo de execução: %sms', int((time_end - time_start) * 1000))

    return result


def __query_builder(query: str, fields: Optional[Dict[str, Any]] = None) -> str:
    """Criar query client incrementando os campos passados pelo dict.
    Tambem efetua uma higienização nos campos.

    :param query: Query Graphql
    :type query: str
    :param fields: Campos desnormalizado
    :type fields: Optional[Dict[str, Any]]
    :return: Query Graphql transformado.
    :rtype: str
    """
    # Imports

    # Transformar query
    if fields:
        query = interpolation(query, dict_to_graphql(fields))
    return query


__all__ = ["request"]
