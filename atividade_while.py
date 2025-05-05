# Atividades

# 1- Crie um programa que receba 5 números
# e retorne a média aritmética entre esses números

soma_dos_numeros = 0
numeros_lidos = 0

while numeros_lidos < 5:  # Cria um laço while
    num_str = input("Digite um valor: ")  # Cria a variável num_str
    # Cria a variavel num_lido. Esta variavel convert num_str eme float
    num_lido = float(num_str)
    soma_dos_numeros += num_lido  # faz a soma dos numeros
    numeros_lidos += 1

media_aritimetica = soma_dos_numeros/5
# executa a funçõa print da soma dos números com o valor exibindo duas cass decimais
print(f"A soma dos números é {media_aritimetica:.2f}")


# 2 - Crie um programa que receba 5 números,
# realiza a soma destes números, mas caso um destes números seja negativo
# não considere ele na soma.

numeros_recebidos = 0
contador = 0

while contador < 5:
    numero_digitado = input("Digite um número: ")
    numero_digitado = float(numero_digitado)

    if numero_digitado < 0:
        contador += 1
        continue
    else:
        numeros_recebidos += numero_digitado
        contador += 1

print(f"A soma dos números é {numeros_recebidos:.2f}")

# 3 - Cria um programa que receba um número arbitrário (definido pelo usuário)
# de números que serão lidos e retorne a soma de todos eles.


# 4 - Percorra os números de 2 até 10 e diga se o número é par ou impar.

# 5- Crie um programa que receba como input uma string.
# Em seguida percorra a string e diga quantos espaços em branco essa string tem.
