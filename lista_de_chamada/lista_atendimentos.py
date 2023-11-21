# Importa a biblioteca random
import random


#Cria a nova LIsta de Analistas
lista_inicial = ['David Alves', 'Felipe Carvalho', 'Giselly Vieira', 'Gleyson Atanazio', 'Jefferson Costa' ,
'José Lucas',
'Leo Martins',
'Lucas Fontenele',
'Madson Rafael',
'Mayanne Ribeiro',
'Nickolas Azevedo',
'Sidynelson',
'Thiago Robson',
'Ira Oliveira',
'Uilliam Santos',
'Rafael Souza',
'Carlos Rocha',
'Nara Silva',
'Shimon Pericles',
'Emerson Nolasco',
'Luiz Teles',
'Carlos Ponte']

for i, elemento in enumerate(lista_inicial):
    print(i, elemento)

print("-------------------------------------")

#Escolhe um Analista Aleatório para Atendimento
analista_escolhido = random.choice(lista_inicial)

for i, analista in enumerate(lista_inicial):
    if analista == analista_escolhido:
        print(f'Analista Escolhido  {i} = {analista}')

print("-------------------------------------")

#Remove o Analista Escolhido
lista_inicial.remove(analista_escolhido)


new_list = []


for i,elemento in enumerate(lista_inicial):
    new_list.append(elemento)
    print(i,elemento)

print(lista_inicial)
print(analista_escolhido)    
print (new_list)
