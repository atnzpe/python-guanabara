lista = ['Maria', 'José', 'Silva']
# inclui um item na lista
lista.append('João')


indices = range(len(lista))

for nomes in lista:
    print(lista.index(nomes))

for i in indices:
    print(i)

# usando a função enumerate para listaR indice e objeto da lista
# Você pode dar um start  para começar de um indice especifico
# Exemplo enumerate(lista, start=1)


for item in enumerate(lista):
    print(item)

# listando os objetos de uma lista
print('listando os objetos de uma lista')
for indice, nomes in enumerate(lista):
    print(nomes)