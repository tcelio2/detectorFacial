from Objects.Tamanho import Tamanho


class Matrix:
    def __init__(self, olho: Tamanho):
        self.olho = olho

    def mostrar(self):
        print(self.olho.getAltura(),self.olho.getBase())