__all__ = [
    "to_string"
]

def to_string(json: dict) -> str:
    """
    Converte um dict para json/string
    Parameters
    ----------
    json: dict
        Objeto dict que será tranformado em json/string
    Returns
    -------
    str
        Objeto json como string
    """
    if not isinstance(json, dict):
        return ''

    import json as modj
    from modules.utils import strings as mods

    textnew = modj.dumps(json, ensure_ascii=True)
    textnew = mods.clean_all(textnew)

    return textnew
