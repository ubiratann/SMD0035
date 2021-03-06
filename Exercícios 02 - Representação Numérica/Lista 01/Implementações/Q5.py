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

base = int(input('Insira a base >> '))
if base <= 1:
    print('A base inserida tem que ser maior que 1')
else:
    if(base > len(LISTA_SIMBOLOS)):
        print('Este algoritmo não suporta uma base tão grande de representação ')
    else:
        numero = input('Insira o número >> ')
        print(f'{numero} convertido da base decimal para a base {base} é : {converter_decimal_base_b(base,numero)}')
