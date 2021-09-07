'''
    Executar o codigo em: https://berinhard.github.io/pyp5js/pyodide/
'''


p1 = {'x': 220, 'y': 320}
p2 = {'x': 100, 'y': 50}

p3 = {'x': 140, 'y': 110}
p4 = {'x': 50, 'y': 200}


def verificarPonto(p1, p2):
    '''
    Função que verifica se 2
    '''
    return (p1['x'] != p2['x'] or p1['y'] != p2['y'])


def verificarAH(p1, p2, p3):
    '''
    Função que verifica se o angulo é Anti-horário
    '''
    return ((p3['y'] - p1['y']) * (p2['x'] - p1['x'])) > ((p2['y'] - p1['y']) * (p3['x'] - p1['x']))


def verificarCruzamento(p1, p2, p3, p4):
    '''
    Função que verifica o cruzamento entre as retas
    '''
    retorno = (verificarAH(p1, p3, p4) != verificarAH(p2, p3, p4)) and (
        verificarAH(p1, p2, p3) != verificarAH(p1, p2, p4))
    return retorno


def setup():
  createCanvas(600, 600)


def draw():
  background('#FAFAFA')

  line(p1['x'], p1['y'], p2['x'], p2['y'])
  stroke(255, 0, 0)
  strokeWeight(1)
  line(p3['x'], p3['y'], p4['x'], p4['y'])
  strokeWeight(1)
  stroke(0, 0, 255)

  if(verificarPonto(p1, p2) and verificarPonto(p3, p4)):
    if(verificarCruzamento(p1, p2, p3, p4)):
        text('As retas se cruzam', 10, 250)
    else:
      text('As retas não se cruzam', 10, 250)
  else:
    text('Você não inseriu retas válidas :(', 10, 250)
    fill(0, 0, 0)
