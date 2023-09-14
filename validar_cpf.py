"""
Cáculo do Primeiro Dígito CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros digitos so CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10. 

"""
cpf = "74682489070"
#cpf = input()
contador = 0


"""Colete a soma dos 9 primeiros digitos so CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10. """

#contador
countdown = 10
#Lista dos nove primeiros numeros
nine_first_numbers = []

#Percorre o CPF multiplicando cada item por um contagem regressiva e alimenta a lista
for i in cpf:
    number_multiplies_by_ten = int(i)*(countdown)
    nine_first_numbers.append(number_multiplies_by_ten)
    countdown -=1
#Obtem os nove primeiros numeros multiplicados pela contagem regressiva de 10 até zero
nine_first_numbers = nine_first_numbers [:9]

#Cria uma variável que soma todos os itens da lista
sum_nine_first_numbers = sum(nine_first_numbers)

#Multiplica a variavel sum_nine_first_numbers por 10
multiplie_sum_nine_first_numbers = sum_nine_first_numbers * 10

#Obter o resto da divisão de multiplie_sum_nine_first_numbers por 11
resto_multiplie = multiplie_sum_nine_first_numbers % 11

print('Resultado é 0' if resto_multiplie > 9 else f'resultado é {resto_multiplie}')

   

 