import pprint #Importa o Módulo do Print Bonito


lista = [n for n in range(10) if n > 0 and n <= 5] #Cria uma lista compreemsion filtrando apos o for com IF menor iguala 5

print(lista) #Imprime a lista filtrada

#Lista de nome Produtos
produtos = [
    {'nome': 'Uva', 'preco': 10,},
    {'nome': 'Laranja', 'preco': 20,},
    {'nome': 'Pera', 'preco': 30,},
]

#MApeamneto da Lista com dados alterados
novos_produtos = [
    {**produto, 'preco': (produto['preco'] + (produto['preco'] * 0.15))}
    if produto['preco'] > 20 else {**produto} #if e else ternário
    for produto in produtos
    if produto ['preco'] > 10 # Filtrando itens com preço maior que 10
]


#Mapeia e deixa os produtos com 15 % de acrescimo
produto_preco_maior = [
    {**produto, 'preco': (produto['preco'] + (produto['preco'] * 0.15))}
    for produto in produtos
]

#produto_preco_menor #

print(*produto_preco_maior, sep='\n')

print(*novos_produtos, sep='\n')