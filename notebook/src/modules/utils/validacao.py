""" 
Utilitarios de Validação. 
""" 
import re 
 
from random import randint 
 
# Lista de palavras para evitar o Titlecase 
LISTA_TITLE = ['da', 'de', 'di', 'do', 'du', 'para', 'no', 'na', 'e'] 
 
 
# Tipo de variavel 
TYPE_STR = type("") 
TYPE_INT = type(0) 


def iptu_sp_verificar_dac(iptu) -> str:
    """ 
    O número-base do IPTU contém 10 dígitos, dos quais os 3 primeiros  
    indicam o SETOR onde o imóvel está localizado dentro da cidade,  
    os três seguintes a QUADRA dentro do Setor e os quatro últimos o  
    LOTE dentro da Quadra. O DV corresponde ao resto da divisão por 11 do  
    somatório da multiplicação de cada algarismo da base  
    respectivamente por 9, 8, 7, 6, 5, 4, 3, 2, 1 e 10 
    Nota: 
    Se o resto for 10 o DV será 1. 
    Parameters 
    ---------- 
    iptu: str or int 
        Numero do IPTU. 
    Response 
    -------- 
    str 
        Retorna iptu somente números se validado ou '' (vazio) se inválido 
    """ 
     
    # Somente caracteres de 0 a 9 são mapeados 
    iptu = ''.join(re.findall('\d', str(iptu))) 
 
    if (not iptu) or (len(iptu) > 11): 
        return False 
 
    if len(iptu) != 11: 
        iptu = iptu.zfill(11) 
     
    iptu_text = "{0:011d}".format(int(iptu)) 
    dac = iptu_text[10:11] 
    iptu_text = iptu_text[0:10] 
 
    total = 0 
    calc = 10 
 
    for digito in iptu_text: 
        total += int(digito) * calc 
        calc = (calc + 1) % 10 
 
    resto = str((total % 11))[0] 
    if resto == dac: 
        # Retorna o valor sem pontos e traços - somente caracteres 
        return ''.join(iptu_text) + str(dac) 
    else: 
        return '' 
     
 
def cnpj_validar_dac(cnpj) -> bool: 
    """  
    Valida CNPJs, retornando apenas a string de números válida. 
    Parameters 
    ---------- 
    iptu: str or int 
        Numero do CNPJ. 
    Response 
    -------- 
    str 
        Retorna iptu somente números se validado ou '' (vazio) se inválido 
    """ 
    # Somente caracteres de 0 a 9 são mapeados 
    cnpj = ''.join(re.findall('\d', str(cnpj))) 
 
    if (not cnpj) or (len(cnpj) > 14): 
        return '' 
 
    if len(cnpj) != 14: 
        cnpj = cnpj.zfill(14) 
 
    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam 
    inteiros = list(map(int, cnpj)) 
    novo = inteiros[:12] 
     
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2] 
    while len(novo) < 14: 
        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11 
        if r > 1: 
            f = 11 - r 
        else: 
            f = 0 
        novo.append(f) 
        prod.insert(0, 6) 
 
    # Se o número gerado coincidir com o número original, é válido 
    if novo == inteiros: 
        # Retorna o valor sem pontos e traços - somente caracteres 
        retorno = '' 
        for i in novo: 
            retorno += str(i) 
        return retorno 
    else: 
        return '' 
 
 
def cpf_validar_dac(cpf) -> str: 
    """  
    Valida CPFs, retornando apenas a string de números válida. 
    Parameters 
    ---------- 
    iptu: str or int 
        Numero do CPF. 
    Response 
    -------- 
    str 
        Retorna iptu somente números se validado ou '' (vazio) se inválido 
    """ 
    # Somente caracteres de 0 a 9 são mapeados 
    cpf = ''.join(re.findall('\d', str(cpf))) 
 
    if (not cpf) or (len(cpf) > 11): 
        return cnpj_validar_dac(cpf) 
 
    if len(cpf) != 11: 
        cpf = cpf.zfill(11) 
 
    # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam 
    inteiros = list(map(int, cpf)) 
    novo = inteiros[:9] 
 
    if len(cpf) > 11: 
        retorno = cnpj_validar_dac(cpf) 
        return retorno 
    else: 
        while len(novo) < 11: 
            r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11 
            if r > 1: 
                f = 11 - r 
            else: 
                f = 0 
            novo.append(f) 
 
        # Se o número gerado coincidir com o número original, é válido 
        if novo == inteiros: 
            # Retorna o valor sem pontos e traços - somente caracteres 
            retorno = '' 
            for i in novo: 
                retorno += str(i) 
            return retorno 
        else: 
            return '' 
 

def cap_name(name: str) -> str:  
    """  
    Capitaliza a primeira letra do nome evitando palavras como 'de', 'do' 
    Parameters 
    ---------- 
    name: str 
        Nome a ser transformado. 
    Response 
    -------- 
    str 
        Retorna nome com a primeira letra de cada palavra 
    """ 
 
    items = [] 
    if name != '' and name != None: 
        for item in name.split(): 
            if not item in LISTA_TITLE: 
                item = item.capitalize() 
            items.append(item) 
        return ' '.join(items) 
    else: 
        return name 


"""
def main(): 
 
     
    #for k in range(0,11): 
             
            iptu_text = '0140750371' 
 
            #for i in range(0,10): 
            #    inteiro = 9 #randint(0,9) 
            #    iptu_text += str(inteiro) 
 
            iptu_text = "{0:010d}".format(int(iptu_text)) 
            iptu_text = iptu_text[0:10] 
 
            total = 0 
            calc = 10 
 
            for digito in iptu_text: 
                total += int(digito) * calc 
                calc = (calc + 1) % 10 
 
            resto = str((total % 11))[0] 
            print (iptu_text + '-' + str(resto)) 
 
if __name__ == "__main__": 
    main() 
 
"""
