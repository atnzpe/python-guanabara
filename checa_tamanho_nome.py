"""
FAça um programa que peça o primeiro nome do usuário. Se o  nome tiver 4 letras ou menos
excreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva seu nome é normal; maior que 6 6 escreva 
"Seu nome é muito grande"

"""


try:

    name = input("Digte seu nome: ")
    size_name = len(name)

    if size_name.isdigit():
        print("seu nome tem numeros")
    if size_name <= 1:
        print("Digite mais que uma letra. ")
    elif size_name >= 2 and size_name <= 4:
        print("Seu nome é curto.")
    elif size_name >= 5 and size_name <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande!")  
   
except:
    print("So tem espaços!")

     



