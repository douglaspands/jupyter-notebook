"""
Utilitarios para funções assincronas.
"""
__all__ = [
    'run'
]


def run(coroutine_):
    """
    Execução do modulo assincrono de forma sincrona.
    É tratado o retorno de uma execução de função async,
    :param coroutine_:
    :return: Resultado a função assincrona.
    """
    import asyncio
    import nest_asyncio
    nest_asyncio.apply()

    async def wrapper_async(promise_, callback_):
        """
        Wrapper para retornar resultado a função assincrona
        :param promise_: Ou couroutine: É uma promessa de entrega.
        :param callback_: Ou future: É um função que será executada quando finalizado o processamento.
        :return:
        """
        callback_.set_result(await promise_)

    # Criando "Event-Loop".
    loop = asyncio.get_event_loop()
    # Criando função de callback.
    future = asyncio.Future()
    # Informando que resultado da função é uma "coroutine" ou "promise".
    asyncio.ensure_future(wrapper_async(coroutine_, future))
    # Ficar em loop até o resultado da função retornar.
    loop.run_until_complete(future)
    # Retornando o resultado da função callback.
    return future.result()
