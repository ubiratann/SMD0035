import math


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

        mediaX = minimo.x + maximo.x / 2
        mediaY = minimo.y + maximo.y / 2
        self.centro = Ponto(mediaX, mediaY, 0)
        self.raio = math.sqrt(
            math.pow(maximo.x - mediaX, 2) + math.pow(maximo.y - mediaY, 2))

    def temSobreposicao(self, circulo):
        return (math.sqrt(math.pow(self.centro.x, circulo.centro.x), 2)
                + math.pow(self.centro.y, 2)) < (circulo.raio + self.raio)

    def dentroDoCirculo(self, ponto):
        return(math.sqrt(math.pow(self.centro.x - ponto.x, 2)
               + math.pow(self.centro.y - ponto.y, 2)) <= self.raio)


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
        return not(elemento.maximo.x > self.maximo.x or elemento.maximo.y > self.maximo.y
                   or elemento.maximo.z > self.maximo.z
                   or elemento.minimo.x < self.minimo.x
                   or elemento.minimo.y < self.minimo.y
                   or elemento.minimo.z < self.minimo.z)


def setup():
    createCanvas(700, 700)


def draw():
    background(0)

    stroke(255)
    noFill()

    strokeWeight(8)
    stroke(255, 0, 0)

    ponto1 = Ponto(50, 300, 0)
    ponto2 = Ponto(80, 80, 0)
    ponto3 = Ponto(200, 230, 0)
    ponto4 = Ponto(100, 190, 0)

    ponto5 = Ponto(50, 300, 0)
    ponto6 = Ponto(80, 80, 0)

    circulo1 = Circulo([ponto1, ponto2, ponto3, ponto4])
    pontoDentroCirculo1 = Ponto(400, 100, 0)

    point(ponto1.x, ponto1.y)
    point(ponto2.x, ponto2.y)
    point(ponto3.x, ponto3.y)
    point(ponto4.x, ponto4.y)

    #  //PONTOS DO OBJETO 2
    stroke(0, 255, 0)
    point(p6.x, p6.y)
    point(p7.x, p7.y)
    point(p8.x, p8.y)
    point(p9.x, p9.y)

    #//PONTO PARA TESTE DO PONTO DENTRO DO CIRCULO
    stroke(200, 0, 122)
    point(p10.x, p10.y)

    strokeWeight(1)
    stroke(120, 120, 0)
    circle(
        b_circle1.center.x,
        b_circle1.center.y,
        2*b_circle1.radius
    )

    circle(
        b_circle2.center.x,
        b_circle2.center.y,
        2*b_circle2.radius
    )
