"""
SQS - Utilitarios customizados
"""
__all__ = [
    "parse_postgres_replication_message", 
    "parse_message",
    "time_delay"
]

import json
import logging

logger = logging.getLogger(__name__)


def parse_postgres_replication_message(message: dict) -> dict:
    """
    Transforma a mensagem que esta no evento em dict.
    Aceita o formato de mensagem da fila de replicacao do Postgres.
    Parameters
    ----------
    message : dict
        Evento recebido pelo SQS.
    Returns
    -------
    dict
        Evento completamente acessivel do tipo dict.
    """
    response = json.loads(message['Messages'][0]['Body'])
    response['Message'] = json.loads(response['Message'])
    response["data"] = {
        "kind": response["Message"]["default"]["kind"],
        "schema": response["Message"]["default"]["schema"],
        "table": response["Message"]["default"]["table"],
        "fields": {}
    }
    for index, item in enumerate(response["Message"]["default"]["columnnames"]):
        response["data"]["fields"][item] = response["Message"]["default"]["columnvalues"][index]
    return response["data"]["fields"]


def parse_message(message: dict) -> dict:
    """
    Extrai somente os dados da mensagem.
    Parameters
    ----------
    message : dict
        Evento recebido pelo SQS.
    Returns
    -------
    dict
        Dados da mensagem.
    """
    response = json.loads(message['Messages'][0]['Body'])
    return response


def time_delay(fibonacci_order: int) -> int:
    """
    Calculo do tempo de delay para publicar mensagem.
    Maximo 900 seg que é equivalente a 15 min.
    Parameters
    ----------
    fibonacci_order: int
        Ordem da sequencia de Fibonacci.
    Returns
    -------
    int
        Quantidade de segundo para passar no Delay do SQS.
    """
    try:
        if fibonacci_order < 1:
            return 60
        elif fibonacci_order > 7:
            return 900
        from .sequence import get_fibonacci
        valor = get_fibonacci(fibonacci_order)
        delay = valor * 60
        return delay
    except:
        logger.debug(f'{__name__}: Em falha, é retornado o valor 60.')
        return 60
