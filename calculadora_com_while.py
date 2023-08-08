""" Calculadora com While 

Permite apenas adição, subtraçõa, multiplicaçõa e divisão


"""

while True:
    n1 = input("Digite um número1: ")
    n2 = input("Digite o segundo número2: ")
    operador = input('Digite a opeçõa que deseja (+-/*): ')

    numeros_validos = None
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
        print('ta no try')
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos. ')         
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas uma operação!')
        continue

    if '+' in operador:
        soma = n1_float+n2_float
        print(f"A soma é {soma}")
        continue
    
    sair = input("Quer sair? [s]im: ").lower().startswith('s') #deixa tudo minisculo e se começar com s retorna um True.
    print(sair)

    if sair:
        break

