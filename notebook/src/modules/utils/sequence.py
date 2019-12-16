"""
Sequencias.
"""
__all__ = ["get_fibonacci"]

def get_fibonacci(n: int) -> int:
    """
    A partir da ordem, é gerado a sequencia de Fibonacci.
    Parameters
    ----------
    n: int
        Numero da ordem.
    Returns
    -------
    int
        Sequencia de Fibonacci.
    """
    from math import sqrt
    try:
        return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
    except TypeError:
        return 0