import math
ALTURA_CANVAS = 500
LARGURA_CANVAS = 500


'''
 executar colando o codigo em: https://berinhard.github.io/pyp5js/pyodide/
'''


class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.prdEscalar(self))

    def verificarNulo(self):
        return self.x == 0 and self.y == 0 and self.z == 0

    def normalizar(self):
        norma = self.norma()
        if norma > 0:
            retorno = Vetor(self.x/norma, self.y/norma, self.z/norma)
            return retorno

    def prdEscalar(self, vetor):
        return self.x * vetor.x + self.y * vetor.y + self.z * vetor.z

    def prdVetorial(self, vetor):
        retorno = Vetor(self.y * vetor.z - self.z * vetor.y,
                        self.z * vetor.x - self.x * vetor.z,
                        self.x * vetor.y - self.y * vetor.x)
        return retorno

    def anguloEscalar(self, vetor):
        retorno = self.prdEscalar(vetor)
        retorno = max(-1, retorno) if retorno < 0 else min(1, retorno)
        return math.degrees(math.acos(retorno))

    def anguloVetorial(self, vetor):
        retorno = self.prdVetorial(vetor)
        return math.degrees(math.asin(retorno.norma() / (self.norma() * vetor.norma())))

    def draw(self):
        stroke(3)
        point(self.x, self.y)
        strokeWeight(3)
        line(0, 0, self.x, self.y)
        strokeWeight(1)


def setup():
    createCanvas(LARGURA_CANVAS, ALTURA_CANVAS)


def draw():
    background('#a4aba6')

    stroke('rgba(190,0,0,0.75)')

    vetorX = Vetor(width, 500, 0)
    vetorY = Vetor(mouseX, mouseY, 0)

    vetorX.draw()
    vetorY.draw()
    if(vetorY.x <= LARGURA_CANVAS and vetorY.x >= 0 and vetorY.y <= ALTURA_CANVAS and vetorY.y >= 0):

        if(vetorX.verificarNulo() == False and vetorY.verificarNulo() == False):
            vetorX = vetorX.normalizar()
            vetorY = vetorY.normalizar()
            text('Angulo pelo produto escalar {}'.format(
                vetorX.anguloEscalar(vetorY)), 150,  250)
            text('Angulo pelo produto vetorial {}'.format(
                vetorX.anguloVetorial(vetorY)), 150, 270)
    else:
        text('MOUSE FORA DO CANVAS', 150, 250)
