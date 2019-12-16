"""
Utilitarios para tratamento de query no GraphQL
"""


def graphilify(dict_: dict = None) -> dict:
    """Transformar o "dict" em um "dict graphile"
    
    :param dict_: dict desnormalizado
    :type dict_: dict
    
    :return: dict normalizado para graphile
    :rtype: dict
    """
    # Validar parametros de entrada passado
    if not isinstance(dict_, dict):
        raise Exception('É obrigatorio passar um parametro no formato "dict"')
    
    # Import
    import json
    
    # Preparando resultado
    dict_new = dict()
    
    # Tratar dicionario
    def tratar_dicionario(d_: dict) -> str:
        dict_text = '{'
        for i_, k_ in enumerate(d_):
            if i_ > 0:
                dict_text += ', '
            if isinstance(d_.get(k_), dict) or isinstance(d_.get(k_), list):
                dict_text += f'{k_}: ' + json.dumps(json.dumps(d_.get(k_)))
            else:
                dict_text += f'{k_}: ' + json.dumps(d_.get(k_))
        dict_text += '}'
        return dict_text
    
    # Tratar lista
    def tratar_lista(l_: list) -> str:
        list_text = '['
        for i_, v_ in enumerate(l_):
            if i_ > 0:
                list_text += ', '
            if isinstance(v_, dict) or isinstance(v_, list):
                list_text += json.dumps(json.dumps(v_))
            else:
                list_text += json.dumps(v_)
        list_text += ']'
        return list_text
    
    # Iterar por todo o dicionario
    for key_ in dict_:
        if isinstance(dict_.get(key_), dict):
            dict_new.update({key_: tratar_dicionario(dict_.get(key_))})
        elif isinstance(dict_.get(key_), list):
            dict_new.update({key_: tratar_lista(dict_.get(key_))})
        else:
            dict_new.update({key_: json.dumps(dict_.get(key_))})
            
    # Retorno
    return dict_new


def interpolation(text: str = None, dict_: dict = None) -> str:
    """Executa a interpolação de textos.

    :param text: Texto com parametros de interpolação disponiveis.
    :type dict_: str

    :param dict_: Dicionario com campos que substituirão o texto passado.
    :type dict_: dict

    :return: Texto substituido pelos campos passados.
    :rtype: str
    """
    # Validar parametros de entrada passado
    if not isinstance(text, str) or not isinstance(dict_, dict):
        raise Exception('Parametros de entrada estão invalidos!')
    
    # Import
    import re
    
    # Resultado
    text_new = text
    
    # Iteração
    for key in re.findall(r'{{\s*\w+\s*}}', text):
        key_ = re.sub(r'{{\s*(\w+)\s*}}', r'\1', key)
        text_new = re.sub(key, dict_.get(key_, 'null'), text_new)
        
    # Retorno
    return text_new


def flatten_graphile(obj_: dict) -> dict:
    """
    Reduz hierarquias do dict. (Utilizando regras do Postgraphile)
    *obs.: Coleções: Sera considerado o primeiro dict. O restante será removido.

    :param obj_: Dicionario com multiplos nós.
    :type obj_: dict
    
    :return: Dicionario com linear
    :rtype: dict 
    """
    # Validação
    if not obj_ or not isinstance(obj_, dict):
        return dict()
    # Novo dict
    obj_new = dict()
    # Para cada key, tratar os sub-nós
    for key in obj_:
        if isinstance(obj_[key], dict):
            obj_new.update(flatten_graphile(obj_[key]))
        elif isinstance(obj_[key], list) and len(obj_[key]) > 0 and isinstance(obj_[key][0], dict):
            obj_new.update(flatten_graphile(obj_[key][0]))
        elif obj_[key] is None:
            continue
        else:
            obj_new[key] = obj_[key]
    # Resultado
    return obj_new


def flatten(data: dict, always_text: bool = False) -> dict:
    """
    Achatar objetos
    :param data: Dicionario com multiplos nós.
    :type data: dict
    :param always_text: Valores sempre no formato texto (Default: False)
    :type always_text: bool
    :return: Dicionario com linear
    :rtype: dict 
    """
    import json
    always_text = always_text if isinstance(always_text, bool) else False
    result = dict()

    def recurse(cur, prop):
        if not isinstance(cur, (list, tuple, dict)):
            result[prop] = json.dumps(cur, default=str) if always_text is True and not isinstance(cur, str) else cur
        elif isinstance(cur, (list, tuple)):
            if len(cur) < 1:
                result[prop] = list()
            else:
                for i, v in enumerate(cur):
                    recurse(v, f'{prop}.{i}' if prop else f'{i}')
        else:
            is_empty = True
            for p, v in cur.items():
                is_empty = False
                recurse(v, f'{prop}.{p}' if prop else p)
            if is_empty:
                result[prop] = dict()

    recurse(data, '')
    return result
