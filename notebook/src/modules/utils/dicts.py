def dict_to_keyhash(d: dict, replace_latin_characters: bool = False) -> dict:
    """
    Unificar niveis do dict.
    """
    import json
    from . import strings
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            result.update(dict_to_keyhash(value, replace_latin_characters))
        elif isinstance(value, list):
            list_text = json.dumps(value)
            list_text = strings.remove_tab_newline(list_text)
            list_text = strings.text_normalize(list_text)
            if replace_latin_characters:
                list_text = strings.replace_latin_characters(list_text)
            result[key] = list_text
        elif isinstance(value, str):
            text = value
            text = strings.remove_tab_newline(text)
            text = strings.text_normalize(text)
            if replace_latin_characters:
                text = strings.replace_latin_characters(text)
            result[key] = text
        else:
            result[key] = str(value)

    return result


def multidictproxy_to_dict(mdp) -> dict:
    """
    Converte MultiDictProxy em Dict.
    :param mdp:
    :type mdp: MultiDictProxy
    :return:
    :rtype: dict
    """
    import logging
    logger = logging.getLogger(__name__)
    try:
        result = dict()
        for key, value in mdp.items():
            result[key] = value
        return result
    except Exception as error:
        logger.error(repr(error))
        return dict()


def flatten_depth(obj_: dict) -> dict:
    """
    Reduz hierarquias do dict.
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
            obj_new.update(flatten_depth(obj_[key]))
        elif isinstance(obj_[key], list) and len(obj_[key]) > 0 and isinstance(obj_[key][0], dict):
            obj_new.update(flatten_depth(obj_[key][0]))
        else:
            obj_new[key] = obj_[key]
    # Resultado
    return obj_new


def flatten(data: dict, always_text: bool = False) -> dict:
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