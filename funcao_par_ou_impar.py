def par_ou_impar(numero):
    
    if numero % 2 == 0:
        print(f'Número {numero} é par!')
    else:
        print(f'Número {numero} é impar!')


number = int(input('Digite um número inteiro: '))

par_ou_impar(number)