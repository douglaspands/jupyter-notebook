
def parse_dict_to_hstore(dict_obj: dict) -> object:
    """
    parse dict para hstore
    Parameters
    ----------
    dict_obj: dict
        Objeto dict que será feito o parse.
    Return
    ------
    object
        Será retornado um objeto "hstore";
    """
    if not isinstance(dict_obj, dict):
        raise Exception(f"{__name__}: Não foi recebido um dict como parametro de entrada")
    
    from sqlalchemy.dialects.postgresql import array, hstore

    list_keys = []
    list_values = []
    for key, value in dict_obj.items():
        list_keys.append(key)
        list_values.append(value)

    hs = hstore(array(list_keys), array(list_values))
    return hs
