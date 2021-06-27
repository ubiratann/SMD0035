import string
LISTA_SIMBOLOS = list(string.digits) + list(string.ascii_uppercase)

def converter(base,numero):
    retorno = 0
    for i in range len(numero)):
        print(f'{numero.index(i)} numero ')
        print(f'{LISTA_SIMBOLOS.index(i)} simbolo')
        retorno += numero.index(i) ** LISTA_SIMBOLOS.index(i)
    print(retorno)
    return retorno

base = int(input('Insira a base >> '))
if(base > len(LISTA_SIMBOLOS)):
    print(f'Este algoritmo não suporta uma base tão grande de representação :`( ')
numero = input('Insira o número >> ')
print(numero)
convercao = converter(base,numero)
