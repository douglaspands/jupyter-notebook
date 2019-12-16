__title__        = 'utils'
__description__  = 'Modulos/Utilitarios para diversos tratamentos de dados'
__url__          = 'www.imovel.ai'
__version__      = '1.13.0'
__author__       = 'Douglas Panhota'
__author_email__ = 'douglas.panhota@imovel.ai'
__copyright__    = 'Copyright 2019, imóvel.aí'
__dependencies__ = ['pydash==4.7.5', 'nest_asyncio==1.2.0']
__changelog__    = """
#************************************************************************************
# data: 2019-12-13      autor: douglas.panhota@ape11.com.br          versao: 1.13.0
# @dicts.flatten
# Achatar dict
#************************************************************************************
# data: 2019-12-03      autor: douglas.panhota@ape11.com.br          versao: 1.12.2
# @collections.balance_line
# Executa o merge de 2 collections.
#************************************************************************************
# data: 2019-12-03      autor: douglas.panhota@ape11.com.br          versao: 1.12.1
# @xmls.create_element
# Função perdida com merge;
#************************************************************************************
# data: 2019-11-28      autor: douglas.panhota@ape11.com.br          versao: 1.12.0
# @graphqls.get_token
# Simplicar o acesso ao token da API GraphQL;
#************************************************************************************
# data: 2019-11-04      autor: douglas.panhota@ape11.com.br          versao: 1.11.0
# @traceback.trace_error
# Retornar trace de erro;
#************************************************************************************
# data: 2019-11-04      autor: douglas.panhota@ape11.com.br          versao: 1.10.1
# @asyncio.run
# Inclusão do modulo nest_asyncio;
#************************************************************************************
# data: 2019-10-14      autor: douglas.panhota@ape11.com.br          versao: 1.10.0
# @strings.interpolation
# Melhorias no algoritmo da função;
#************************************************************************************
# data: 2019-08-16      autor: douglas.panhota@imovel.ai              versao: 1.9.0
# @strings.b64encode
# Transformar texto em base64.
#************************************************************************************
# data: 2019-08-09      autor: douglas.panhota@imovel.ai              versao: 1.8.0
# @dicts.flatten_depth
# Conversor de multidictproxy para dict.
#************************************************************************************
# data: 2019-07-26      autor: douglas.panhota@imovel.ai              versao: 1.7.0
# @dicts.multidictproxy_to_dict
# Conversor de multidictproxy para dict.
#************************************************************************************
# data: 2019-07-26      autor: douglas.panhota@imovel.ai              versao: 1.7.0
# Inclusão do modulo asyncios.
# @asyncios.run
# Função para tratar resultado de funções async como sync.
#************************************************************************************
# data: 2019-06-16      autor: douglas.panhota@imovel.ai              versao: 1.5.0
# Remoção de modulo não usados.
# Ajuste nos testes unitarios.
# @xmls.dict_to_xml
# Geração de XML através do dict.
#************************************************************************************
# data: 2019-06-10      autor: douglas.panhota@imovel.ai              versao: 1.4.0
# @strings.replace_tags
# incluir valor default caso o campo não seja identificado.
# Inclusão da dependencia da lib "pydash".
#************************************************************************************
# data: 2019-05-17      autor: douglas.panhota@imovel.ai              versao: 1.3.1
# @validacao
# Restaurado atualizações perdidas na validação.
#************************************************************************************
# data: 2019-05-17      autor: douglas.panhota@imovel.ai              versao: 1.3.0
# @sqs.time_delay
# Inclusao de função que utiliza a sequencia de Fibonnacci para calcular o tempo
# de delay para envio para publicação na fila. Maximo de 900 seg (15 min).
# @strings.search_text
# Inclusao de tratamento para caracteres do tipo escape.
#************************************************************************************
# data: 2019-05-14      autor: douglas.panhota@imovel.ai              versao: 1.2.0
# @strings.unicode_normalize
# Inclusao de tratamento de caracteres
# @strings.search_text
# Pesquisa de palavras em textos
#************************************************************************************
# data: 2019-05-13      autor: douglas.panhota@imovel.ai              versao: 1.1.1
# @dicts.dict_to_keyhash
# Inclusão da opção de remoção de caracteres.
# @strings.replace_latin_characters
# Inclusão da função para substituição de caracteres em latin.
# Será substituidos vogais com acentos para vogais sem acentos por exemplo.
#************************************************************************************
# data: 2019-05-13      autor: douglas.panhota@imovel.ai              versao: 1.0.0
# Inicio do versionamento
#************************************************************************************
"""
