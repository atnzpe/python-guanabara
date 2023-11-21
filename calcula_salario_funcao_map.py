'''
Você trabalha em um programa de folha de pagamento.

Dada uma lista de salários, você precisa pegar o bônus que todos estão recebendo
como entrada e aumentar todos os salários por esse valor.

Exiba a lista resultante.

Você pode usar a função map() para aumentar todos os valores da lista.

'''




salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input("Digita o valor do bonus: "))

new_salaries = list(map(lambda x: x + bonus,salaries))
print(new_salaries)