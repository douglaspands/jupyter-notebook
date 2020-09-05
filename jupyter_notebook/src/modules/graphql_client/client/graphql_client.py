""" GraphClient
"""
__all__ = ["GraphQLClient"]
from typing import Optional, Dict, Any

from . import core
from .types import IGraphQLResponse

class GraphQLClient:
    """GraphQLClient
    """
    def __init__(self, url: str):
        """
        Construtor
        :param url: Rota de onde vai ser executado a api em GraphQL
        :type url: str
       """
        self.__url = url
        self.__authorization: Optional[str] = None

    def set_token(self, token: Optional[str]) -> "GraphQLClient":
        """
        Atribuir token.
        :param token: Token (Sem o 'Bearer')
        :type token: str
        :return: GraphQLClient
        :rtype: self
        """
        self.__authorization = token if isinstance(token, str) else None
        return self

    def query(
            self,
            query: str,
            fields: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = 3.001,
            ensure_ascii: Optional[bool] = True,
    ) -> IGraphQLResponse:
        """
        Executa a query do GraphQL.
        :param query: Query do GraphQL
        :type query: str
        :param fields: (opcional) Parametros que farão a interpolação do GraphQL
        :type fields: dict
        :param timeout: (opcional) Tempo em segundos para disparar o timeout
        :type timeout: float
        :param ensure_ascii: Garantir conversão ASCII. (default: True)
        :type ensure_ascii: bool
        :return: Resultado da request
        :rtype: dict
        """
        return core.request(
            url=self.__url,
            query=query,
            fields=fields,
            authorization=self.__authorization,
            timeout=timeout,
            ensure_ascii=ensure_ascii,
        )
