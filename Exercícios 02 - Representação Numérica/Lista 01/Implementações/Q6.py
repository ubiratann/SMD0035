import string
LISTA_SIMBOLOS = list(string.digits) + list(string.ascii_uppercase)

def converter_entre_bases(base_a,base_b,numero_base_a):
    """função de conversão genérica"""
    numero_decimal = converter_base_x_decimal(base_a,numero_base_a)
    if(base_b == 10) return numero_decimal
    numero_base_b = converter_decimal_base_(base_b,numero_decimal)
    return numero_base_b

def converter_base_x_decimal(base,numero):
    """ função que converte e retorna um número da base x para decimal"""
    retorno = 0
    expoente = 0
    retorno = 0
    for i in range(len(numero)-1, -1,-1):
        numero_dec = LISTA_SIMBOLOS.index(numero[i]) #valor a ser convertido da string
        retorno += numero_dec * (base ** expoente)
        expoente += 1
    return retorno


def converter_decimal_base_x(base,numero):
    """função que converte e retorna um número da base decimal para uma base x"""
    retorno = 0
    expoente = 0
    retorno = ''
    while(numero > 0):
        resto = numero % base
        digito_b = LISTA_SIMBOLOS[resto]
        retorno = f'{digito_b}{retorno}'
        numero //= base
    return retorno

base = int(input('Insira a base do número >> '))
if(base < 0):
    print('Base inválda')
if(base > len(LISTA_SIMBOLOS)):
    print('Este algoritmo não suporta uma base tão grande de representação ')
numero = input(f'Insira o número na base {base} >> ')
base = int(input('Insira a base do número >> '))

conversao = converter_base_b_decimal(base,numero)
print(conversao)
