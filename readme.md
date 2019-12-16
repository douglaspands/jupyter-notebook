# Jupyter Notebook

## Instalação Padrão

```shell
pip install jupyter matplotlib autopep8 nest_asyncio jupyter_contrib_nbextensions
```
```shell
jupyter contrib nbextension install --user
```
> Sempre é aconselhavel utilizar um ambiente virtual para o Python3. Ex.: `virtualenv`.

## Configurações Iniciais
```shell
jupyter notebook --generate-config
```
Vai gerar um arquivo de configurações, para personalizar caso seja necessario.

## Acesso a modulos compartilhados
Dentro do Jupyter Notebook
```
import os, sys,
sys.path.insert(0, os.path.abspath('./src'))
```
## Extras

Caso necessite usar funções `async` (utilizando o event loop), é necessario importar um modulo com um patch do  **Jupyter** antes dentro do `notebook`:

```shell
import nest_asyncio
nest_asyncio.apply()
```

## Modulos Importantes

```shell
pip install pydash requests graphqlclient pandas beautifulsoup4 selenium boto3
```

## Modulos Extras

### NLP

```shell
pip install wordcloud nltk seaborn
```
```shell
python -m nltk.downloader averaged_perceptron_tagger floresta mac_morpho machado punkt stopwords wordnet words
```

### Whatsapp

```shell
pip install twilio
```

## PIP - Atualização de Modulos

```shell
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```
