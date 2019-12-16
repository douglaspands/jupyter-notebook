
def get_token(info) -> str:
    """
    Obter token de APIs GraphQL.
    :param info: Objeto recebido pelo GraphQL Server
    :return: token
    :rtype: str
    """
    try:
        token = info.context.get('request').headers.get('Authorization').replace('Bearer ', '')
    except:
        token = ''
    return token
