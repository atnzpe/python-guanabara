# Atividade operações Aritimeticas

a = '''
>> Atividade 1
Crie um programa que possui duas variáveis, 
uma recebe o ano em que estamos e outra o ano em que você nasceu. 
Em seguida subtraia ambas para receber uma estimativa de quantos anos você tem. 
Mostre esse valor na saida do programa. 
'''
print(a)

try:
    ano_atual = int(input("Digite o ano atual: "))
    ano_nasc = int(input("Digite o ano de nascimento: "))
    anos = ano_atual - ano_nasc
    print(f'Você tem {anos} anos')

except ValueError:
    print("Digite somente números!")

a = '''
>> Atividade 2
Crie um programa que faz a média aritmética entre très números.
Estes números devem ser salvos em uma variável.
Mostre esse valor na saída do programa.
'''

print(a)

n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
n3 = float(input('Digite nota 3: '))
media = (n1+n2+n3)/3

print(f'A média é: {media}')

a = '''
>> Atividade 3
Crie um programa que calcule o IMC (indice de massa corporal).
O IMC é dado pelo peso em KG divido pela altura em metros elevado ao quadrado.
Salvar esses valores em uma variável.
Mostre esse valor na saida do programa.
'''
print(a)

peso = float(input('Digite o peso: '))
altura = float (input('Digite a altura em cm. (Ex: 178)): '))

imc = peso/(altura * altura)

print (f'Seu IMC é: {imc:2.2f}')




'''
4 (Desafio) Você tem um determinado números de ovos de páscoa para dividir entre um determinado número de pessoas (duas variáveis iniciais). Determine quantos ovos ficarão por pessoa e quantos ovos sobrarão pois não puderam ser divido igualmente. 
Lembre o número de ovos por pessoa é um número inteiro.
'''
