def par_ou_impar(numero):
    if numero % 2 == 0:
        return print(f"Número {numero} é PAR!")
    return print(f"Número {numero} é IMPAR!")


print(str.title("\nExibe se o numero é PAR ou IMPAR\n"))
number = int(input("Digite um número inteiro: "))

par_ou_impar(number)
