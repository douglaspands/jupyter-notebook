"""
Modulo de Report
"""
import logging

logger = logging.getLogger(__name__)
report_list = dict()


def push(name: str, msg: str):
    """
    Adicionar no relatorio
    :param name: Nome do relatorio
    :param msg: Mensagem para armazenar
    :return: Sem retorno
    """
    if not name or not msg or not isinstance(name, str) or not isinstance(msg, str):
        logger.warning('Parametros de entrada estão invalidos, não foi possivel adicionar ao relatorio')
        return None
    try:
        report_list[name].append(msg)
    except KeyError:
        report_list[name] = list()
        report_list[name].append(msg)


def get(name: str) -> list:
    """
    Obter relatorio no formato de lista.
    :param name: Nome do relatorio
    :return: Lista de mensagens do relatório
    :rtype: list
    """
    if not name or not isinstance(name, str):
        logger.warning('Parametros de entrada estão invalidos, não foi possivel obter o relatorio')
        return list()
    try:
        return report_list[name]
    except KeyError:
        return list()


def get_text(name: str, sep: str = '') -> str:
    """
    Obter relatorio no formato de texto
    :param name: Nome do relatorio
    :param sep: Texto de separação
    :return: Relatório no formato de texto
    :rtype: str
    """
    if not name or not isinstance(name, str):
        logger.warning('Parametros de entrada estão invalidos, não foi possivel obter o relatorio')
        return ''
    try:
        return f'{sep}'.join(report_list[name])
    except KeyError:
        return ''
