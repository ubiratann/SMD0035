import string
LISTA_SIMBOLOS = list(string.digits) + list(string.ascii_uppercase)

def converter_decimal_base_b(base,numero):
    """função que converte e retorna um número da base decimal para uma base b"""
    retorno = 0
    expoente = 0
    retorno = ''
    while(numero > 0):
        resto = numero % base
        digito_b = LISTA_SIMBOLOS[resto]
        retorno = f'{digito_b}{retorno}'
        numero //= base
    return retorno


numero = input('Insira o número >> ')
print(f'{numero} convertido da base decimal para binário é : {converter_decimal_base_b(2,numero)}')
print(f'{numero} convertido da base decimal para octal é : {converter_decimal_base_b(8,numero)}')
print(f'{numero} convertido da base decimal para hexadecimal é : {converter_decimal_base_b(16,numero)}')
