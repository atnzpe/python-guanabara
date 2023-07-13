palavra = input("Digite uma palavra: ")
buscar = input("Digite uma letra ou numero para checar se esta na palavra digitada: ")

if buscar in palavra:
    print(f'{buscar} esta em {palavra}')
else:
    print(f'{buscar} não esta em {palavra}')