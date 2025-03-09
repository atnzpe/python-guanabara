#1 - Crie uma única string que contêm seu nome e sobrenome, 
# em seguida use o slicing para separar o nome em uma variável 
# e o seu sobrenome em outra. 
# Printe esses valores.

#Source
name_complete = input("Digte seu nome e seu sobrenome: ")

# Encontra o índice do espaço em branco para separar o nome e sobrenome
space_index = name_complete.find(" ")

# Usa o slicing para extrair o nome e sobrenome
name = name_complete[:space_index]
surname = name_complete[space_index + 1:]

# Imprime os valores
print("Nome:", name)
print("Sobrenome:", surname)



#2 Leia uma string através do input e retire o ultimo caractere.

palavra = input("Digite uma palavra: ")
palavra_modificada = palavra[:-1] #remove o último caracter

print(palavra)
print(palavra_modificada)


#3 Faça um programa que leia uma string através do input e diga se ela possui uma vogal.

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"

tem_vogal = any(vogal in palavra for vogal in vogais)

if tem_vogal:
    print("A palavra possui uma vogal.")
else:
    print("A palavra não possui uma vogal.")


#4 Faça um programa que insira a palavra 'ABC' na primeira posição de uma string
# lida por input.

word = input("Digite uma palavra: ")
abc = "ABC"

word_final = abc + word

print(word_final)

'''
Explicações detalhadas:

Exercício 1:

Input: A linha name_complete = input("Digte seu nome e seu sobrenome: ") solicita ao usuário que digite seu nome completo.
Encontrando o espaço: space_index = name_complete.find(" ") encontra a posição do primeiro espaço em branco na string digitada pelo usuário.
Slicing:
name = name_complete[:space_index] extrai o nome, que vai do início da string até o espaço.
surname = name_complete[space_index + 1:] extrai o sobrenome, que vai do caractere após o espaço até o final da string.
Print: print("Nome:", name) e print("Sobrenome:", surname) exibem o nome e sobrenome separados.
Exercício 2:

Input: palavra = input("Digite uma palavra: ") pede ao usuário que digite uma palavra.
Remoção do último caractere: palavra_modificada = palavra[:-1] usa slicing para remover o último caractere da palavra ([:-1] significa “todos os caracteres, exceto o último”).
Print: print(palavra) e print(palavra_modificada) exibem a palavra original e a palavra modificada sem o último caractere.
Exercício 3:

Input: palavra = input("Digite uma palavra: ") recebe a palavra do usuário.
Vogais: vogais = "aeiouAEIOU" define uma string com todas as vogais (minúsculas e maiúsculas).
Verificação de vogais: any(vogal in palavra for vogal in vogais) verifica se existe alguma vogal na palavra. Se houver, any() retorna True, caso contrário, retorna False.
Print: A condição if tem_vogal: verifica se a palavra possui uma vogal e imprime a mensagem correspondente.
Exercício 4:

Input: word = input("Digite uma palavra: ") recebe a palavra do usuário.
Concatenação: word_final = abc + word concatena a string “ABC” à palavra digitada, colocando “ABC” no início da string.
Print: print(word_final) exibe a palavra final com “ABC” no início.


'''