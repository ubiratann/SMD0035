from math import sqrt, acos, asin, degrees


class Vetor:
    '''
    Vetor que conta com as seguinte operações:
        @atributo: x -> ponto x do vetor
        @atributo: y -> ponto y do vetor
        @atributo: norma -> norma do vetor
    '''

    def __init__(self, x, y):
        if(x is None or y is None):
            raise ValueError(f'O vetor <{x},{y}> possui uma coordenada nula')
        else:
            self.x = x
            self.y = y
            self.norma = sqrt(self.prdEscalar(self))

    def prdEscalar(self, vetor):
        '''
        Função que retorna o produto escalar de 2 vetores
        '''

        return (self.x * vetor.x) + (self.y * vetor.y)

    def prdVetorial(self, vetor):
        '''
        Função que retorna o produto vetorial entre 2 vetores
        '''

        return Vetor(self.x * vetor.y, self.y * vetor.x)

    def normalizar(self):
        '''
            Função que normaliza o vetor
        '''
        if(self.norma == 0):
            raise ValueError(f'Vetor <{self.x},{self.y}> tem norma 0')
        else:
            return Vetor(self.x / self.norma, self.y / self.norma)


def anguloPrdEscalar(vetorX, vetorY):
    '''
    Função que calcula e retorna o ângulo entre vetores pelo produto escalar
    '''

    produto = vetorX.prdEscalar(vetorY)
    produto = max(-1, produto) if produto < 0 else min(1, produto)
    return degrees(acos(produto))


def anguloPrdVetorial(vetorX, vetorY):
    '''
    Função que calcula e retorna o ângulo entre vetores pelo produto vetorial
    '''

    vetorProduto = vetorX.prdVetorial(vetorY)
    return degrees(asin(vetorProduto.norma / (vetorX.norma * vetorY.norma)))


try:
    vetorX = Vetor(0, 500)
    vetorY = Vetor(-0.0001z, 00)
    print(
        f'Angulo pelo produto escalar: {anguloPrdEscalar(vetorX.normalizar(), vetorY.normalizar())}°')
    print(
        f'Angulo pelo produto vetorial: {anguloPrdVetorial(vetorX.normalizar(), vetorY.normalizar())}°')

except ValueError as ve:
    [print(f'Erro: {msg} !') for msg in ve.args]
