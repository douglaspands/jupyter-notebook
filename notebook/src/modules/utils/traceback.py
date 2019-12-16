
def trace_error() -> str:
    """
    Obter traceback do erro.
    :return: Traceback do erro
    :rtype: str
    """
    import sys
    import traceback
    exc_type, exc_value, exc_traceback = sys.exc_info()
    le = traceback.format_exception(exc_type, exc_value, exc_traceback)
    se = ''.join(le)
    return se
