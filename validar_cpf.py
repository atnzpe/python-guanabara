"""
Cáculo do Primeiro Dígito CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros digitos so CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10.

Ex.: 746.824.890-70 (746824890)
...10..9..8..7..6..5..4..3..2
*..7...4..6..8..2..4..5..0..0
...70..36.48.56.12.20.32.27.0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anteriro por 11
3010 % 11 = 7

Se o resultado for maior que 9:
    resultado é 0
contrario disso:
    resultado é o valor da conta




"""
cpf = "74682489070"
#cpf = input()
contador = 0


"""Colete a soma dos 9 primeiros digitos so CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10. """

#contador regresssivo
countdown = 10
#Lista dos nove primeiros numeros
nine_first_numbers = []

#Percorre o CPF multiplicando cada item por um contagem regressiva e alimenta a lista
for i in cpf:
    number_multiplies_by_ten = int(i)*(countdown)
    nine_first_numbers.append(number_multiplies_by_ten)
    print(i,countdown)
    countdown -=1
#Obtem os nove primeiros numeros multiplicados pela contagem regressiva de 10 até zero
nine_first_numbers = nine_first_numbers [:9]
print(nine_first_numbers)

#Cria uma variável que soma todos os itens da lista
sum_nine_first_numbers = sum(nine_first_numbers)

#Multiplica a variavel sum_nine_first_numbers por 10
multiplie_sum_nine_first_numbers = sum_nine_first_numbers * 10

#Obter o resto da divisão de multiplie_sum_nine_first_numbers por 11
resto_multiplie = multiplie_sum_nine_first_numbers % 11

print(f'Resultado é {resto_multiplie}' if resto_multiplie <= 9 else 0)

   

 