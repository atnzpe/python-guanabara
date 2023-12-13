#Lista de nome Produtos
produtos = [
    {'nome': 'Uva', 'preco': 10,},
    {'nome': 'Laranja', 'preco': 20,},
    {'nome': 'Pera', 'preco': 30,},
]

#Mapeia e deixa os produtos com 15 % de acrescimo
produto_preco_maior = [
    {**produto, 'preco': (produto['preco'] + (produto['preco'] * 0.15))}
    for produto in produtos
]

#produto_preco_menor #

print(*produto_preco_maior, sep='\n')