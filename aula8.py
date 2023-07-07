nome = input('Digite seu nome: ')
sobrenome = str(input('Digite seu sobrenome: '))
idade = int(input('Digite sua idade: '))
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))

if idade > 18:
    maior_de_idade = True
else:
    False        

altura = float(input('Digite sua altura eme metros. Ex: 1.71: '))

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Maior de Idade: ', maior_de_idade)
print('Altura: ', altura)
