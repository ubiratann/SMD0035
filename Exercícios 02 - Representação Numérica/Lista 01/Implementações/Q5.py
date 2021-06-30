import string
LISTA_SIMBOLOS = list(string.digits) + list(string.ascii_uppercase)

def converter_decimal_base_b(base,numero):
    """função que converte e retorna um número da base decimal para uma base b"""
    retorno = 0
    expoente = 0
    retorno = ''
    1234
    2
    while(numero > 0):
        resto = numero % base
        digito_b = LISTA_SIMBOLOS[resto]
        retorno = f'{digito_b}{retorno}'
        numero //= base
    return retorno

print(converter_decimal_base_b(3,213))
