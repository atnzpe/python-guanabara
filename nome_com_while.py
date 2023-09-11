nome = input("Digite seu nome: ")
separador = input("Digite o separador: ")
new_name = ""

if nome.isalpha():
    i = 0  # contador loop while

    while i < len(nome):
        # print(nome[i])
        letra = nome[i]
        new_name += separador + letra
        i += 1
else:
    new_name = nome
    print(f'Não digitou somente letras {new_name=}')

new_name += separador
print(f'Seu nome ficará assim {new_name}')
