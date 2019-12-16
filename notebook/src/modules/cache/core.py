"""
Cache In Memory
"""
__all__ = ['get', 'put', 'rem']

import logging
from datetime import datetime, timedelta

# Logger
logger = logging.getLogger(__name__)

# Cache
cache = dict()


def get(key: str) -> any:
    """
    Obter valor da chave do cache.
    :param key: Chave pesquisada no cache.
    :type key: str
    :return: Retornar valor da chave pesquisada no cache.
    :rtype: any
    """
    value = None
    vb = cache.get(key)
    if vb:
        try:
            if not vb.get('expire') or datetime.now().timestamp() < vb.get('expire'):
                value = vb.get('data')
            else:
                rem(key)
        except Exception as error:
            logger.warning(error)
            rem(key)
    return value


def put(key: str, value, ttl: int = None):
    """
    Gravar chave e valor no cache.
    :param key: Chave pesquisada no cache.
    :type key: str
    :param value: Valor.
    :type value: any
    :param ttl: Milissegundo para expirar.
    :type ttl: int
    """
    if not isinstance(key, str):
        raise Exception('Chave invalida!')
    vb = {'data': value}
    if isinstance(ttl, int) and ttl > 0:
        vb['expire'] = (datetime.now() + timedelta(milliseconds=ttl)).timestamp()
    cache[key] = vb


def rem(key: str):
    """
    Remover do cache.
    :param key: Chave para remover.
    :type key: str
    """
    try:
        del cache[key]
    except KeyError:
        pass
