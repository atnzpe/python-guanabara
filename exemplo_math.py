#importa a biblioteca math
import math

#Solicita um numero inteiro e guarda va variavel num
num = int(input("Digite um número: "))

#
raiz_quadrada = math.sqrt(num)

print(f'{raiz_quadrada =:.2f} do número {num}')
print(f'{math.ceil(raiz_quadrada)} do número {num} arredondada para cima')
print(f'{math.floor(raiz_quadrada)} do número {num} arredondada para baixo')
