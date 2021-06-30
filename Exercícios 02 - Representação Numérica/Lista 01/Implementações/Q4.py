import string
LISTA_SIMBOLOS = list(string.digits) + list(string.ascii_uppercase)

def converter_base_b_decimal(base,numero):
    retorno = 0
    expoente = 0
    retorno = 0
    for i in range(len(numero)-1, -1,-1):
        numero_dec = LISTA_SIMBOLOS.index(numero[i]) #valor a ser convertido da string
        retorno += numero_dec * (base ** expoente)
        expoente += 1
    return retorno

base = int(input('Insira a base >> '))
if base <= 1:
    print('A base inserida tem que ser maior que 1')
if(base > len(LISTA_SIMBOLOS)):
    print('Este algoritmo não suporta uma base tão grande de representação ')
convercao = converter_base_b_decimal(base,numero)
print(conversao)
