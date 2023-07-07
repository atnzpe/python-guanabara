nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura. Exemplo: 1.78: "))
peso = float(input("Digite seu peso. Exemplo: 80: "))

imc = round(peso / altura ** 2,2)

print(f'Olá {nome}, seu peso é {peso} Kg, sua altura é de {altura} e seu IMC é {imc}')