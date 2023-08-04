"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

"""

numero = float(input("Digite um numero: "))

#checa_numero = numero == round(numero)

if numero % 2 == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é impar!')

if (numero == round(numero)):
    print(f'{int(numero)} inteiro')
else:
    print(f'{numero} decimal')        

    
#print(numero)
#print(numero.is_integer())