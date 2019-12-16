

def balance_line(col1: list = None, col2: list = None, key: str = None, sort_key: str = None) -> list:
    """
    Concatenar 2 coleções.
    :param col1: Coleção 1
    :type col1: list
    :param col2: Coleção 2
    :type col2: list
    :param key: Chave de concatenação
    :type key: str
    :param sort_key: Chave de classificação após concatenação.
    :type sort_key: str
    :return: Retorna coleção concatenada.
    :rtype: list
    """
    if not isinstance(col1, list) or not isinstance(col2, list) or not isinstance(key, str):
        raise Exception('collections.balance_line: Parametros de entrada invalidos!')

    # Importando pydash
    # noinspection PyProtectedMember
    from pydash import _
    import sys

    try:

        # Ordenando as colections recebidas
        col1s = _.sort(col1.copy(), key=lambda k_: k_.get(key), reverse=True)
        col2s = _.sort(col2.copy(), key=lambda k_: k_.get(key), reverse=True)

        # Coleção que será retornada
        col3 = list()

        # Chaves
        def get_key(col_):
            try:
                return col_.pop().copy()
            except:
                obj_ = dict()
                obj_[key] = sys.maxsize
                return obj_

        # Obtendo objeto com a chave
        key1 = get_key(col1s)
        key2 = get_key(col2s)

        # Efetuar o merge da das 2 collections
        while True:

            # Balance line
            if key1.get(key) == key2.get(key):
                key1.update(key2)
                col3.append(key1)
                key1 = get_key(col1s)
                key2 = get_key(col2s)
            elif key1.get(key) < key2.get(key):
                col3.append(key1)
                key1 = get_key(col1s)
            else:
                key2 = get_key(col2s)
                col3.append(key2)

            # Fim do loop
            if key1.get(key) == key2.get(key) == sys.maxsize:
                break

        # Classificar se foi passado a chave
        if sort_key and isinstance(sort_key, str):
            _.sort(col3, key=lambda k_: str(k_.get(sort_key, '')).zfill(9))

        # Coleção concatenada
        return col3

    except Exception as error:
        raise Exception(f'collections.balance_line: Ocorreu um erro interno: {repr(error)}')
