"""
Nós definimos uma função chamada decor que tem um único parâmetro func.
Dentro de decor, definimos uma função aninhada chamada wrap.
A função wrap irá imprimir uma string, em seguida, chamar func(), e imprimir outra string.
A função decor retorna a função wrap como seu resultado.

Podemos dizer que a variável decorated é uma versão decorada de print_text - é print_text mais algo.

Na verdade, se escrevêssemos um decorador útil, poderíamos querer substituir print_text pela versão decorada de uma vez por todas, para que sempre obtivéssemos nossa versão "mais algo" de print_text.

Isso é feito reatribuindo a variável que contém nossa função:

"""
name_user = input("Digte seu nome: ")
# Cria a funçãoa decor


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def print_name():
    print(f"Seja bem vindo {name_user}!")


print_name = decor(print_name)
print_name()
