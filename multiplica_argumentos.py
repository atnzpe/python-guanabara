#Importa a função prod da biblioteca math. Esse função vai ajudar a multiplicar os elementos da Lista
from math import prod
#Cria a funçõa mult para multiplicar a lisa dos itens
def mult(*args):
    #cria uma variavel chamada produto_list  que multiplica os elementos da lista 
    produto_list = prod(*args)
    #retorna o produto dessa lista  
    return produto_list

lista = []

numero = int(input("Digite um numero: "))
lista.append(numero)

while True:
    resposta = input("Deseja incluir outro numero?/n[s]im ou [n]ão? ")

    if resposta == 's':
        numero = int(input("Digite um numero: "))
        lista.append(numero)
    else:
        break

amor = mult(lista)
print(lista)
print(amor)