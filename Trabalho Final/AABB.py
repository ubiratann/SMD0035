import math

'''
Executar codigo em: https://berinhard.github.io/pyp5js/pyodide/
'''

aabb1 = AABB()
aabb1.ajusteMinMax([Ponto(50, 300, 0), Ponto(80, 80, 0),
                   Ponto(200, 230, 0), Ponto(300, 210, 0)])

aabb2 = AABB()

# COM SOBREPOSICAO
# aabb2.ajusteMinMax([Ponto(150, 400, 0), Ponto(180, 180, 0),
#                   Ponto(300, 330, 0), Ponto(400, 310, 0)])

aabb2.ajusteMinMax([Ponto(650, 400, 0), Ponto(590, 180, 0),
                   Ponto(400, 330, 0), Ponto(400, 310, 0)])


class Ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class AABB:
    def __init__(self):
        self.minimo = Ponto(math.inf, math.inf, math.inf)
        self.maximo = Ponto(-math.inf, -math.inf, -math.inf)

    def ajusteMinMax(self, vertices):
        if len(vertices) == 0:
            return 0
        else:
            for vertice in vertices:
                self.minimo.x = min(vertice.x, self.minimo.x)
                self.maximo.x = max(vertice.x, self.maximo.x)

                self.minimo.y = min(vertice.y, self.minimo.y)
                self.maximo.y = max(vertice.y, self.maximo.y)

                self.minimo.z = min(vertice.z, self.minimo.z)
                self.maximo.z = max(vertice.z, self.maximo.z)

    def temSobreposicao(self, elemento):
        return (not(elemento.minimo.x > self.maximo.x)
                or (elemento.minimo.y > self.maximo.y)
                or (elemento.minimo.z > self.maximo.z)
                or (elemento.maximo.x < self.minimo.x)
                or (elemento.maximo.y < self.minimo.y)
                or (elemento.minimo.z < self.minimo.z))


def setup():
    createCanvas(700, 700)


def draw():
    background('#FAFAFA')

    stroke(255)
    noFill()

    strokeWeight(1)
    stroke(237, 34, 93)
    beginShape()
    noFill()
    vertex(aabb1.minimo.x, aabb1.minimo.y)
    vertex(aabb1.maximo.x, aabb1.minimo.y)
    vertex(aabb1.maximo.x, aabb1.maximo.y)
    vertex(aabb1.minimo.x, aabb1.maximo.y)
    endShape(CLOSE)

    strokeWeight(1)
    stroke(24, 234, 93)
    beginShape()
    noFill()
    vertex(aabb2.minimo.x, aabb2.minimo.y)
    vertex(aabb2.maximo.x, aabb2.minimo.y)
    vertex(aabb2.maximo.x, aabb2.maximo.y)
    vertex(aabb2.minimo.x, aabb2.maximo.y)
    endShape(CLOSE)

    if aabb1.temSobreposicao(aabb2):
        textoSaida = 'Existe sobreposição entre os elementos'
    else:
        textoSaida = 'Não existe sobreposição entre os elementos'

    strokeWeight(1)
    stroke(0, 0, 255)
    fill(0, 0, 0)

    text(textoSaida, 230, 660)
