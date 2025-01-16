from copy import deepcopy

# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00, 'quantidade': 7},
    {'nome': 'Produto 1', 'preco': 22.32, 'quantidade': 5},
    {'nome': 'Produto 3', 'preco': 10.11, 'quantidade': 12},
    {'nome': 'Produto 2', 'preco': 105.87, 'quantidade': 9},
    {'nome': 'Produto 4', 'preco': 69.90, 'quantidade': 70},
]

# Imprime os produtos com os preços atualizados
print("Imprime os produtos com os preços atualizados\n")
for contador in produtos:
    print(f"Nome: {contador['nome']}, Preço: {contador['preco']:.2f}, Qtd: {contador['quantidade']}")

# Aumente os preços dos produtos a seguir em 10%
print('Aumente os preços dos produtos a seguir em 10%\n')

# faz a itração
for contador in produtos:
    # altra a chave preco dentro da lista produtos
    contador['preco'] *= 1.10  # aumenta o preço eme 10%

# Imprime os produtos com os preços atualizados
print("Imprime os produtos com os preços atualizados\n")
for contador in produtos:
    print(f"Nome: {contador['nome']}, Preço: {contador['preco']:.2f}, Qtd: {contador['quantidade']}")

print("\n")

# Gere novos_produtos por deep copy (copia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00, 'quantidade': 7},
    {'nome': 'Produto 1', 'preco': 22.32, 'quantidade': 5},
    {'nome': 'Produto 3', 'preco': 10.11, 'quantidade': 12},
    {'nome': 'Produto 2', 'preco': 105.87, 'quantidade': 9},
    {'nome': 'Produto 4', 'preco': 69.90, 'quantidade': 70},
]

# Crie uma cópia profunda da lista de produtos
print("Crie uma cópia profunda da lista de produtos\n")
copia_profunda_produtos = deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)

produtos_ordenados = sorted(
    copia_profunda_produtos, key=lambda produto: produto['nome'], reverse=True)
# Imprime os produtos ordenados
print("Imprime os produtos ordenados por nome decrescente\n")
for produto in produtos_ordenados:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Qtd: {produto['quantidade']}")

print("\n")

# Gere produtos_ordenados por nome por deep copy (cópia profunda)

produtos_ordenados_nome = deepcopy(produtos)
produtos_ordenados_nome = sorted(
    produtos_ordenados_nome, key=lambda produto: produto['nome'], reverse=True)
# Imprime os produtos ordenados
print("Imprime os produtos ordenados por nome decrescente por deep copy\n")
for produto in produtos_ordenados_nome:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Qtd: {produto['quantidade']}")


print("\n")

# Ordene os produtos por preco crescente (do menor para maior)

produtos_ordenados_preco = deepcopy(produtos)
produtos_ordenados_preco = sorted(
    produtos_ordenados_preco, key=lambda produto: produto['preco'])
# Imprime os produtos ordenados
print("Imprime os produtos ordenados por preco crescente\n")
for produto in produtos_ordenados_preco:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Qtd: {produto['quantidade']}")

print("\n")

# Gere produtos_ordenados por preco por deep copy (cópia profunda)

produtos_ordenados_preco_copia = deepcopy(produtos_ordenados_preco)
# Imprime os produtos ordenados
print("Imprime os produtos ordenados por preco crescente por deep copy\n")
for produto in produtos_ordenados_preco_copia:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Qtd: {produto['quantidade']}")




'''
Explicação do código:

Importar deepcopy:

from copy import deepcopy: Importa a função deepcopy do módulo copy, que é usada para criar cópias profundas de objetos.
Criar a lista de produtos:

produtos = [...]: Define uma lista de dicionários, onde cada dicionário representa um produto com nome, preço e quantidade.
Impressão inicial dos produtos:

Imprime a lista de produtos com os preços e quantidades originais.
Aumentar os preços em 10%:

Itera pela lista produtos usando um loop for.
Para cada produto, multiplica o preço atual por 1.10 (equivalente a adicionar 10%) e atualiza o valor do preço no dicionário.
Imprime a lista de produtos novamente com os preços atualizados.
Geração de novos_produtos por deepcopy:

Cria uma nova lista novos_produtos usando deepcopy(produtos). Isso cria uma cópia profunda da lista produtos, garantindo que alterações em novos_produtos não afetem a lista produtos original.
Ordenação por nome decrescente:

Cria produtos_ordenados usando sorted(copia_profunda_produtos, key=lambda produto: produto['nome'], reverse=True).
sorted: Ordena a lista.
key=lambda produto: produto['nome']: Define a chave de ordenação como o nome do produto.
reverse=True: Ordena em ordem decrescente.
Imprime a lista ordenada.
Geração de produtos_ordenados_nome por deepcopy:

Cria produtos_ordenados_nome como uma cópia profunda de produtos.
Ordena a cópia usando a mesma lógica da etapa anterior.
Imprime a lista ordenada.
Ordenação por preço crescente:

Cria produtos_ordenados_preco como uma cópia profunda de produtos.
Ordena a cópia por preço usando a mesma lógica da etapa anterior, mas sem a opção reverse=True (para ordenação crescente).
Imprime a lista ordenada.
Geração de produtos_ordenados_preco_copia por deepcopy:

Cria produtos_ordenados_preco_copia como uma cópia profunda da lista já ordenada por preço (produtos_ordenados_preco).
Imprime a lista ordenada.
Explicação sobre deepcopy:

deepcopy cria uma cópia completamente independente da estrutura de dados original. Isso é importante quando você precisa modificar uma cópia da lista sem afetar o original. Se você usar copy.copy() (cópia rasa), as alterações em elementos internos da lista (como dicionários) afetariam o original.

Importante: O código completo acima demonstra como usar deepcopy para diferentes cenários de ordenação. Você pode adaptar este código para atender às suas necessidades específicas.



'''