from math import cos, sin
import numpy as np  # so pra printar bonitinho

##############################################################################
##                  INICIO DAS OPERAÇÕES BÁSICAS                            ##
##                                                                          ##
##############################################################################


def somar(matrizA, matrizB):

    if(len(matrizA) != len(matrizB) or len(matrizA[0]) != len(matrizB[0])):
        return 'ESSAS MATRIZES NÃO PODEM SER SOMADAS'
    n = len(matrizA)
    m = len(matrizB[0])

    matrizSoma = []
    for i in range(n):
        matrizSoma.append([])
        for j in range(m):
            matrizSoma[i].append(matrizA[i][j] + matrizB[i][j])

    return matrizSoma


def subtrair(matrizA, matrizB):

    if(len(matrizA) != len(matrizB) or len(matrizA[0]) != len(matrizB[0])):
        return 'ESSAS MATRIZES NÃO PODEM SER SUBTRAIDAS'

    n = len(matrizA)
    m = len(matrizB[0])
    matrizSubtracao = []

    for i in range(n):
        matrizSubtracao.append([])
        for j in range(m):
            matrizSubtracao[i].append(matrizA[i][j] - matrizB[i][j])

    return matrizSubtracao


def multiplicar(matrizA, matrizB):
    if(len(matrizB) != len(matrizA[0])):
        return 'ESSAS MATRIZES NÃO PODEM SER MULTIPLICADAS'
    n = len(matrizA)
    m = len(matrizB[0])
    o = len(matrizB)

    matrizMultiplicacao = []

    for i in range(n):
        matrizMultiplicacao.append([])
        for j in range(m):
            matrizMultiplicacao[i].append(0)
            for k in range(o):
                matrizMultiplicacao[i][j] += matrizA[i][k] * matrizB[k][j]
    return matrizMultiplicacao

##############################################################################
##                  INICIO DAS OPERAÇÕES DE TRANSFORMAÇÃO                   ##
##                                                                          ##
##############################################################################


def translatar(x, y):
    retorno = [[1, 0, x],
               [0, 1, y],
               [0, 0, 1]]

    return retorno


def rotacionar(x):
    retorno = [[cos(x), -sin(x), 0],
               [sin(x),  cos(x), 0],
               [0, 0, 1]]

    return retorno


def escalar(x, y):
    retorno = [[x, 0, 0],
               [0, y, 0],
               [0, 0, 1]]

    return retorno


def trs(angulo, tx, ty, sx, sy):
    retorno = [[cos(angulo) * sx, -sin(angulo) * sy, tx],
               [sin(angulo) * sx,  cos(angulo) * sy, ty],
               [0, 0, 1]]

    return retorno


matrizA = [[1, 2, 3],
           [3, 2, 1]]

matrizB = [[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]]


print('MATRIZ A :::::')
print(np.array(matrizA))
print()

print('MATRIZ B :::::')
print(np.array(matrizB))
print()

print('SOMA ::::')
print(np.array(somar(matrizA, matrizB)))
print()

print('SUBTRAÇÃO ::::')
print(np.array(subtrair(matrizA, matrizB)))
print()

print('MULTIPLICAÇÃO :::')
print(np.array(multiplicar(matrizA, matrizB)))
print()
