import random


class Mazo:
    palos = {'nombres': ['oro', 'copa', 'basto', 'espada'], 'valores': [1, 2, 3, 4]}
    valores = (range(1, 12))

    def __init__(self, nombre='id', descartar=tuple(), rango_valores=(1, 12)):
        self.nombre = nombre
        self.memoria = []
        self.valores = tuple([num for num in range(rango_valores[0], rango_valores[1] + 1) if num not in descartar])
        self.tamaño = len(self.valores) * len(self.palos['nombres'])

    def generar_carta(self):
        while len(self.memoria) < self.tamaño:
            carta = (random.choice(self.valores),
                     random.choice(self.palos['nombres']))
            if carta not in self.memoria:
                self.memoria.append(carta)
                return carta
        return False

    def barajar(self):
        self.memoria = []


if __name__ == '__main__':
    mazoAzul = Mazo(rango_valores=(1, 4), descartar=(2, 5))

    for i in range(10):
        print(mazoAzul.generar_carta())
    print(mazoAzul.memoria)
