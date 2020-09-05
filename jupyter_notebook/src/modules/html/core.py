import re
from typing import Dict, List, Any, Union


def tratar_valor_primitivo(valor: Union[str, int, float, bool]) -> str:
    valor_ = str(valor)
    
    if valor_ == '':
        return 'N/D'
    
    else:
        if bool(re.search(r'^http', valor_)):
            return '<a target="_blank" href="{0}">{0}</a>'.format(valor_)
        
        else:
            return valor_


# Tratar dicionario
def tratar_dict(d: Dict[str, Any], incluir_responsive: bool=False) -> str:

    html_text = '<div class="table-responsive">' if incluir_responsive is True else '<div>'
    html_text += '<table class="table table-striped">'

    for k, v in d.items():
        html_text += '<tr>'
        html_text += '<th scope="row">{0}</th>'.format(k)

        if isinstance(v, (int, str, bool, float)):
            html_text += '<td>{0}</td>'.format(tratar_valor_primitivo(v))

        elif isinstance(v, dict):
            html_text += '<td>{0}</td>'.format(tratar_dict(v, True))

        elif isinstance(v, list):
            
            if len(v) == 0:
                html_text += '<td>N/D</td>'
                
            elif isinstance(v[0], dict):
                html_text += '<td>{0}</td>'.format(tratar_colecao(v))

            else:
                html_text += '<td><ul>'
                for i in v:
                    html_text += '<li>{0}</li>'.format(tratar_valor_primitivo(i))

                html_text += '</ul></td>'
        
        html_text += '</tr>'

    html_text += '</table></div>'
    return html_text


# Tratar lista de dicionarios
def tratar_colecao(l: List[Dict[str, Any]]) -> str:
    html_text = '<div class="table-responsive"><table class="table table-striped"><thead><tr>'
    for k in l[0].keys():
        html_text += '<th scope="col">{0}</th>'.format(k)
        
    html_text += '</tr></thead><tbody>'
    for i in l:
        html_text += '<tr>'
        for v in i.values():
            if isinstance(v, (int, str, bool, float)):
                html_text += '<td>{0}</td>'.format(tratar_valor_primitivo(v))
                
            else:
                html_text += '<td>{0}</td>'.format(tratar_dict(v, True))
        
        html_text += '</tr>'
                        
    html_text += '</tbody></table></div>'
    return html_text


# Construir HTML
def construir_html(dados: Dict[str, Any], titulo: str = 'SEM TITULO') -> str:
    """
    Construir HTML.
    """
    html = """
    <html><head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"></head>
    <body><div class="container-fluid"><header><h1>#TITULO#</h1></header><section>
    """.strip().replace('#TITULO#', titulo)
    html += tratar_dict(dados)
    html += '</section></div></body></html>'
    
    return html
