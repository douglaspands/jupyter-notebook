import os
import json
import pandas as pd
from pandas import DataFrame
from modules.utils import dicts


def gerar_dataframe(lista: list, colunas: list = None) -> DataFrame:
    lista_ = lista if isinstance(lista, list) else [lista]
    colunas = colunas if isinstance(colunas, list) and len(colunas) > 0 else None
    lista_dfs = [DataFrame([linha_], columns=(colunas if colunas else linha_.keys())) for linha_ in lista_]
    return pd.concat(lista_dfs, ignore_index=True, sort=False)

def dataframe_to_csv(df: DataFrame, path: str):
    path_full = os.path.join('/home/imovelai/apps/jupyter/files', f'{path}.csv')
    df.to_csv(path_full, index = None, header=True, sep=";")

def file_write(data, path: str):
    path_full = os.path.join('/home/imovelai/apps/jupyter/files', f'{path}.json')
    with open(path_full, 'w') as out:
        out.write(json.dumps(data, default=str, ensure_ascii=True, indent=2))

def apresentacao(dados, path: str) -> DataFrame:
    if isinstance(dados, list):
        fr = list(map(lambda d_: dicts.flatten(d_), dados))
    elif isinstance(dados, dict):
        fr = dicts.flatten(dados)
    else:
        raise Exception('É possivel apresentar apenas variaveis do tipo "dict" e "list".')
    df = gerar_dataframe(fr)
    if path and isinstance(path, str):
        dataframe_to_csv(df, path)
        file_write(dados, path)
    return df
