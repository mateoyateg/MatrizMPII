import numpy as np


def mostrar(matriz):

    print(matriz[0])

    if len(matriz[1:,:]) is not 0:
        mostrar(np.rot90(matriz[1:, :]))


def cargarTexto():
    return [x.split() for x in open("matriz.txt").readlines()]


if __name__ == '__main__':
    print ("Matriz original:")
    print np.array(cargarTexto())
    print("")

    print ("Matriz recorrida en forma de caracol: ")
    mostrar(np.array(cargarTexto()))
