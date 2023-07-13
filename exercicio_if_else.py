primeiro_numero = input("Digite um número: ")
segundo_numero = input("Digite outro número: ")

n1 = int(primeiro_numero)
n2 = int(segundo_numero)

if n1 > n2:
    print(f'{n1} maior que {n2}')
elif n1 < n2:
    print(f'{n1} menor que {n2}')
elif n1 != n2:
    print(f'{n1} não é igual {n2}')
else:
    print(f'{n1} igual a {n2}')

print('Fim do exercicio')