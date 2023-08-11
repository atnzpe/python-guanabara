import os

secret_word = input("Digite uma palavra secreta: ")
tam = len(secret_word)

for i in range(tam):
    print('Limpando a Tela')
    os.system("cls")


letra_digitada = input("1 while Digite uma letra: ")

# tamanho_letra_digitada = len(letra_digitada)
n_tentativas = 0

while n_tentativas <= 3:

    if letra_digitada in secret_word:
        print(f'{letra_digitada=}')
        print('Parabens tu acertou!!')

    else:
        while n_tentativas <= 3:

            print(f' "*" . Voce tem {n_tentativas} Tentativas')
            letra_digitada = input(
                'Advinhe a letra que esta na palavra secreta: ')

            if letra_digitada in secret_word:
                print(f'{letra_digitada=}')

            n_tentativas += 1    

        print(f'Você usou {n_tentativas} Tentativas!')
        

    print(f'Você usou {n_tentativas} Tentativas!')
    

    # deixa tudo minisculo e se começar com s retorna um True.
    #if n_tentativas >= 0 and 
    
    sair = input("Quer sair? [s]im: ").lower().startswith('s')
    print(f'Você digitou "{sair}"')
    if sair:
        print("Até logo!")
        break
    else:
        n_tentativas = 0
        continue


    # if tamanho_letra_digitada > 1:
    #   letra_digitada = input("while menor que 1 Digite uma letra: ")

# if letra_digitada in secret_word:
#    print(letra_digitada)
# else:
#    while n_tentativas <= 3:
#        print(f'Voce tem {n_tentativas} Tentativas')
#        letra_digitada = input('Advinhe a letra que esta na palavra secreta: ')
#        n_tentativas += 1

        # if n_tentativas == '3':
        #   break
