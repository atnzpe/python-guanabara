qtd_linhas = input("Digite o numero de linhas: ")
qtd_colunas = input("Digite o numero de colunas: ")

if qtd_linhas.isnumeric() and qtd_colunas.isnumeric():
    linha = 1

    while linha <= int(qtd_linhas):
        coluna = 1
        while coluna <= int(qtd_colunas):
            print(f'imprime a {linha=} da {coluna=}')
            coluna += 1
        linha += 1
else:
    print(f'Não digitou apenas numeros {qtd_colunas=} {qtd_linhas=}')
