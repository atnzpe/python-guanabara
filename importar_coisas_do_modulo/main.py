# Importa o modulo completo
import modulo
#Importa um pedaço do modulo
from modulo import variavel_modulo
from sys import path

print('l3 Este arquivo se chama', __name__)
print('L4',modulo)
print(variavel_modulo)

print("\n\nLista o PATH\n\n")

print(*path, sep='\n')