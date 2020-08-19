from Objects.Aluno import Aluno
from Objects.Matrix import Matrix
from Objects.Tamanho import Tamanho

t = Tamanho(1, 44)


a:int = t.getBase()
b:int = t.getAltura()

print (a+b)

m = Matrix(t)
m.mostrar()