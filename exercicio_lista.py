# Exercicio
# Peça para usuário digitar seu nome
nome = input("Digite seu nome: ")
# Peça ao usuario para digitar sua idade:
idade = input("Digite sua idade: ")


# Se nome e idade forem digitados:
if nome and idade:
    # exiba
    print(f"Seu nome é '{nome}'")  # Exibe o nome
    print(f"Seu nome invertido é '{nome[::-1]}'")  # Exibe o nome invertido

    if ' ' in nome:
        print(f"O '{nome=}' contém espaços em branco!")
    else:
        print(f"O '{nome}' não contem em branco espaços!")

    print(f"Seu nome tem '{len(nome)}' letras")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é '{nome[len(nome)-1]}'")

else:
    if nome == "":
        print(f'O nome esta eme branco = {nome=}')
    elif idade == "":
        print(f'A idade esta em branco = {idade=}')
    else:
        print(f'Deixo o {nome=} e a {idade=} em branco!')
