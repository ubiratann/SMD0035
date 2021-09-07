import math

'''
Executar codigo em: https://berinhard.github.io/pyp5js/pyodide/
'''


ponto1 = Ponto(50, 300, 0)  # fora do circulo
ponto2 = Ponto(80, 80, 0)  # fora do circulo
ponto3 = Ponto(200, 230, 0)  # fora do circulo
ponto4 = Ponto(300, 210, 0)  # dentro do ciculo
circulo1 = Circulo([Ponto(310, 100, 0)])


class Ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Circulo:

    def __init__(self, vertices):
        self.calcularCentroRaio(vertices)

    def calcularCentroRaio(self, vertices):
        minimo = Ponto(math.inf, math.inf, 0)
        maximo = Ponto(-math.inf, -math.inf, 0)

        if(len(vertices) == 0):
            return 0
        else:
            for vertice in vertices:
                minimo.x = min(vertice.x, minimo.x)
                maximo.x = max(vertice.x, maximo.x)

                minimo.y = min(vertice.y, minimo.y)
                maximo.y = max(vertice.x, maximo.y)

        mediaX = (minimo.x + maximo.x) / 2
        mediaY = (minimo.y + maximo.y) / 2
        self.centro = Ponto(mediaX, mediaY, 0)
        self.raio = math.sqrt(
            math.pow(maximo.x - mediaX, 2) + math.pow(maximo.y - mediaY, 2))

    def temSobreposicao(self, circulo):
        return (math.sqrt(math.pow(self.centro.x, circulo.centro.x), 2)
                + math.pow(self.centro.y, 2)) < (circulo.raio + self.raio)

    def dentroDoCirculo(self, ponto):
        return(math.sqrt(math.pow(self.centro.x - ponto.x, 2)
               + math.pow(self.centro.y - ponto.y, 2)) <= self.raio)


def setup():

    createCanvas(700, 700)


def draw():
    background('#FAFAFA')

    stroke(255)
    noFill()

    strokeWeight(8)
    stroke(255, 0, 0)

    point(ponto1.x, ponto1.y)
    strokeWeight(1)
    stroke(0, 0, 255)
    fill(0, 0, 0)
    text('p1', ponto1.x + 5, ponto1.y)

    stroke(255)
    noFill()
    strokeWeight(8)
    stroke(255, 0, 0)

    point(ponto2.x, ponto2.y)
    strokeWeight(1)
    stroke(0, 0, 255)
    fill(0, 0, 0)
    text('p2', ponto2.x + 5, ponto2.y)

    stroke(255)
    noFill()
    strokeWeight(8)
    stroke(255, 0, 0)

    point(ponto3.x, ponto3.y)
    strokeWeight(1)
    stroke(0, 0, 255)
    fill(0, 0, 0)
    text('p3', ponto3.x + 5, ponto3.y)

    stroke(255)
    noFill()
    strokeWeight(8)
    stroke(255, 0, 0)
    point(ponto4.x, ponto4.y)

    strokeWeight(1)
    stroke(0, 0, 255)
    fill(0, 0, 0)
    text('p4', ponto4.x + 5, ponto4.y)

    stroke(255)
    noFill()
    strokeWeight(8)
    stroke(255, 0, 0)

    strokeWeight(1)
    stroke(120, 120, 0)
    circle(
        circulo1.centro.x,
        circulo1.centro.y,
        2*circulo1.raio
    )

    if circulo1.dentroDoCirculo(ponto3):
        textoSaida = 'O ponto está dentro do circulo '
    else:
        textoSaida = 'O ponto não está dentro do circulo '

    strokeWeight(1)
    stroke(0, 0, 255)
    fill(0, 0, 0)

    text(textoSaida, 230, 660)
